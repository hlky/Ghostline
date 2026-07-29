# Ghostline Test Quests

Each `gqt###` directory owns its implementation generator and world
specification:

```text
gqt###/
└── implementation/
    ├── build.py
    └── world/
        └── descriptive-name.world.json
```

The typed `.quest.json` manifests remain at this directory's root for now.
Generic quest compilers, scene/world generators, and shared content helpers
remain under `tools`.
