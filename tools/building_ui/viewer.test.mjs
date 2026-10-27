import test from 'node:test';
import assert from 'node:assert/strict';
import { BuildingViewer } from './viewer.js';

test('repeated shell instances subscribe once per pending mesh', async () => {
  const viewer = Object.create(BuildingViewer.prototype);
  Object.assign(viewer, { moduleErrors: new Set(), moduleRefreshes: new Set() });
  const resolvers = new Map();
  let requests = 0, refreshes = 0;
  viewer.moduleAsset = id => {
    requests++;
    return new Promise(resolve => resolvers.set(id, resolve));
  };
  viewer.scheduleUpdate = () => refreshes++;
  for (let rebuild = 0; rebuild < 10; rebuild++) {
    for (let instance = 0; instance < 137; instance++) viewer.requestModule('asset-' + instance % 21);
  }
  assert.equal(requests, 21);
  for (const resolve of resolvers.values()) resolve({});
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(refreshes, 21);
  assert.equal(viewer.moduleRefreshes.size, 0);
});

test('completed loads coalesce into one rebuild using the current floor', () => {
  const viewer = Object.create(BuildingViewer.prototype);
  Object.assign(viewer, { refreshFrame: null, sceneData: {}, options: { level: 0 } });
  const old = globalThis.requestAnimationFrame;
  let scheduled = 0, callback, updated;
  globalThis.requestAnimationFrame = fn => { scheduled++; callback = fn; return 1; };
  viewer.update = (scene, options) => { updated = options.level; };
  try {
    for (let i = 0; i < 137; i++) viewer.scheduleUpdate();
    viewer.options = { level: 2 };
    assert.equal(scheduled, 1);
    callback();
    assert.equal(updated, 2);
    assert.equal(viewer.refreshFrame, null);
    viewer.disposed = true;
    viewer.scheduleUpdate();
    assert.equal(scheduled, 1);
  } finally { globalThis.requestAnimationFrame = old; }
});

test('failed mesh requests stop retrying and report one error', async () => {
  const viewer = Object.create(BuildingViewer.prototype);
  Object.assign(viewer, { moduleErrors: new Set(), moduleRefreshes: new Set() });
  let requests = 0, errors = 0;
  viewer.moduleAsset = () => { requests++; return Promise.reject(new Error('missing')); };
  viewer.onStatus = () => errors++;
  viewer.requestModule('missing');
  await new Promise(resolve => setImmediate(resolve));
  viewer.requestModule('missing');
  assert.equal(requests, 1);
  assert.equal(errors, 1);
});

test('reference materials are shared across rebuilds without changing solid materials', () => {
  const viewer = Object.create(BuildingViewer.prototype);
  viewer.materials = {};
  const ref = viewer.material('wall', 'default', true);
  for (let i = 0; i < 137; i++) assert.equal(viewer.material('wall', 'default', true), ref);
  const solid = viewer.material('wall', 'default');
  assert.notEqual(ref, solid);
  assert.equal(ref.transparent, true);
  assert.equal(solid.transparent, false);
  ref.dispose(); solid.dispose();
});
