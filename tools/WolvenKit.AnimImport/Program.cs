using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using System.Text;
using WolvenKit.CLI.Services;
using WolvenKit.Common;
using WolvenKit.Common.Interfaces;
using WolvenKit.Common.Model;
using WolvenKit.Common.Model.Arguments;
using WolvenKit.Common.Services;
using WolvenKit.Core.Compression;
using WolvenKit.Core.Interfaces;
using WolvenKit.Core.Services;
using WolvenKit.Modkit.RED4;
using WolvenKit.RED4.CR2W;
using WolvenKit.RED4.CR2W.Archive;
using WolvenKit.RED4.Archive.CR2W;
using WolvenKit.RED4.Archive.IO;
using WolvenKit.RED4.Types;
using static WolvenKit.RED4.Types.Enums;

if (args.Length is not (3 or 4))
{
    Console.Error.WriteLine(
        "Usage: WolvenKit.AnimImport <game-root> <input.anims.glb> <output-directory> [target-rig-depot-path]"
    );
    return 2;
}

var gameRoot = Path.GetFullPath(args[0]);
var glb = new FileInfo(Path.GetFullPath(args[1]));
var output = new DirectoryInfo(Path.GetFullPath(args[2]));
var targetRig = args.Length == 4 ? args[3] : null;
var executable = new FileInfo(
    Path.Combine(gameRoot, "bin", "x64", "Cyberpunk2077.exe")
);
if (!executable.Exists || !glb.Exists || !output.Exists)
{
    Console.Error.WriteLine("Game executable, GLB, or output directory does not exist.");
    return 2;
}
if (!Oodle.Load())
{
    Console.Error.WriteLine("WolvenKit could not load an Oodle library.");
    return 1;
}

var services = new ServiceCollection();
services.AddLogging(builder => builder.AddSimpleConsole(options =>
{
    options.SingleLine = true;
    options.TimestampFormat = "HH:mm:ss ";
}));
services.AddScoped<ILoggerService, MicrosoftLoggerService>();
services.AddScoped<IProgressService<double>, PercentProgressService>();
services.AddSingleton<IHashService, HashService>();
services.AddSingleton<ITweakDBService, TweakDBService>();
services.AddSingleton<ILocKeyService, LocKeyService>();
services.AddSingleton<IHookService, HookService>();
services.AddScoped<Red4ParserService>();
services.AddSingleton<IArchiveManager, ArchiveManager>();
services.AddSingleton<IModTools, ModTools>();

await using var provider = services.BuildServiceProvider();
var archiveManager = provider.GetRequiredService<IArchiveManager>();
archiveManager.LoadGameArchives(executable);

if (!string.IsNullOrWhiteSpace(targetRig))
{
    var redFilePath = Path.Combine(
        output.FullName,
        Path.GetFileNameWithoutExtension(glb.Name)
    );
    if (!File.Exists(redFilePath))
    {
        Console.Error.WriteLine($"No existing redfile found to retarget: {redFilePath}");
        return 1;
    }

    var parser = provider.GetRequiredService<Red4ParserService>();
    CR2WFile? animsArchive;
    using (var input = File.OpenRead(redFilePath))
    {
        animsArchive = parser.ReadRed4File(input);
    }
    if (animsArchive is not { RootChunk: animAnimSet anims })
    {
        Console.Error.WriteLine($"Existing redfile is not an animAnimSet: {redFilePath}");
        return 1;
    }

    anims.Rig = new CResourceReference<animRig>((ResourcePath)targetRig);
    using var rewritten = new MemoryStream();
    using (var writer = new CR2WWriter(rewritten, Encoding.UTF8, true)
    {
        LoggerService = provider.GetRequiredService<ILoggerService>(),
    })
    {
        writer.WriteFile(animsArchive);
    }
    File.WriteAllBytes(redFilePath, rewritten.ToArray());
    Console.WriteLine($"Retargeted animset rig to {targetRig}");
}

var importArgs = new GltfImportArgs
{
    AdditiveStripLocalTransform = true,
    Keep = true,
    ImportFormat = GltfImportAsFormat.Anims,
};
var settings = new GlobalImportArgs().Register(
    new CommonImportArgs { Keep = true },
    importArgs
);
var raw = new RedRelativePath(glb.Directory!, glb.Name);
var modTools = provider.GetRequiredService<IModTools>();
var ok = await modTools.Import(raw, settings, output, true);
return ok ? 0 : 1;
