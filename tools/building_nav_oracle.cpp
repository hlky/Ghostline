// Offline Detour compatibility oracle. This does not invoke Cyberpunk's AI.
#include "DetourNavMesh.h"
#include "DetourNavMeshQuery.h"
#include "DetourAlloc.h"
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>

static_assert(sizeof(dtMeshHeader) == 100, "VAND header layout differs");
static_assert(sizeof(dtPoly) == 20, "VAND triangle layout differs");
static_assert(sizeof(dtLink) == 16, "VAND link layout differs");
static_assert(sizeof(dtOffMeshConnection) == 40, "VAND offmesh layout differs");

int main(int argc, char** argv) {
    if (argc < 9) return 2;
    const int tileCount = std::atoi(argv[1]);
    if (tileCount < 1 || tileCount > 256 || argc != tileCount + 8) return 2;
    dtNavMesh nav;
    dtNavMeshParams params{};
    params.tileWidth = params.tileHeight = 32.4f;
    params.maxTiles = std::max(tileCount * 2, 16);
    params.maxPolys = 65536;
    if (dtStatusFailed(nav.init(&params))) return 3;
    for (int i = 0; i < tileCount; ++i) {
        std::ifstream file(argv[i + 2], std::ios::binary);
        if (!file) return 4;
        std::vector<unsigned char> input((std::istreambuf_iterator<char>(file)), {});
        auto* data = static_cast<unsigned char*>(dtAlloc(input.size(), DT_ALLOC_PERM));
        if (!data) return 5;
        std::memcpy(data, input.data(), input.size());
        const dtStatus status = nav.addTile(data, static_cast<int>(input.size()), DT_TILE_FREE_DATA, 0, nullptr);
        if (dtStatusFailed(status)) {
            dtFree(data);
            std::cout << "{\"loaded\":false,\"status\":" << status << "}\n";
            return 6;
        }
    }
    dtNavMeshQuery query;
    if (dtStatusFailed(query.init(&nav, 32768))) return 7;
    float start[3], end[3];
    for (int i = 0; i < 3; ++i) {
        start[i] = std::strtof(argv[tileCount + 2 + i], nullptr);
        end[i] = std::strtof(argv[tileCount + 5 + i], nullptr);
    }
    const float extents[] = {.3f, .1f, .3f};
    dtQueryFilter filter;
    dtPolyRef first = 0, last = 0;
    float firstPoint[3]{}, lastPoint[3]{};
    query.findNearestPoly(start, extents, &filter, &first, firstPoint);
    query.findNearestPoly(end, extents, &filter, &last, lastPoint);
    dtPolyRef path[4096]{};
    int count = 0;
    dtStatus status = 0;
    if (first && last) status = query.findPath(first, last, firstPoint, lastPoint, &filter, path, &count, 4096);
    const dtMeshTile* firstTile = nullptr;
    const dtMeshTile* lastTile = nullptr;
    const dtPoly* ignored = nullptr;
    if (first) nav.getTileAndPolyByRef(first, &firstTile, &ignored);
    if (last) nav.getTileAndPolyByRef(last, &lastTile, &ignored);
    const bool reachable = first && last && !dtStatusFailed(status) && count > 0 && path[count - 1] == last
        && std::abs(firstPoint[1] - start[1]) < .15f && std::abs(lastPoint[1] - end[1]) < .15f;
    std::cout << "{\"loaded\":true,\"start_found\":" << (first ? "true" : "false")
              << ",\"end_found\":" << (last ? "true" : "false")
              << ",\"reachable\":" << (reachable ? "true" : "false")
              << ",\"start_layer\":" << (firstTile ? firstTile->header->layer : -1)
              << ",\"end_layer\":" << (lastTile ? lastTile->header->layer : -1)
              << ",\"start_height_error\":" << std::abs(firstPoint[1] - start[1])
              << ",\"end_height_error\":" << std::abs(lastPoint[1] - end[1])
              << ",\"path_polygons\":" << count << ",\"status\":" << status << "}\n";
    return 0;
}
