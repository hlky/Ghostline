# Ghostline Quest Template

Use a stable `gq###` directory. Omit files that a smaller quest does not need.

```text
gq###/
├── README.md
├── flow.md
├── continuity.md
├── acts/
│   └── 01-descriptive-name.md
├── script/
│   ├── 01-descriptive-name.md
│   ├── readables.md
│   └── voice-notes.md
├── voice/
│   ├── generate-auditions.py
│   └── source/
└── implementation/
    ├── build.py
    ├── quest.json
    ├── state.md
    ├── assets.md
    ├── plan.md
    ├── scenes/
    │   └── descriptive-name.scene-spec.json
    └── world/
        └── descriptive-name.world.json
```

`flow.md` owns stage ordering and IDs. Act files own local gameplay intent,
entry/exit state, and failure handling. `script/` owns exact player-facing
words. `implementation/quest.json`, when present, is the compiler manifest.
Quest-specific generators and scene/world specifications stay under
`implementation`; generic compilers and serializers stay under `tools`.
The checked starter world specification is
`implementation/world/example.world.json`.
