# Change Log

All notable changes to the XASM Toolkit extension are documented here.

## 0.1.2

- Added syntax highlighting for the XASM `.DS` storage directive.
- Made highlighting case-insensitive for 6502 instructions, XASM directives and pseudo-instructions, including paired instructions such as `InY:bNe` and opcode expressions such as `{nOp}`.
- Removed the system Node.js requirement for **Build & Run (detached)** and **Run only (detached)** on Linux. Existing projects can adopt the fix by updating the two Linux entries in `.vscode/launch.json` as described in the README.
- Disabled editor color previews for XASM files in the example workspace and in newly generated workspace settings.

## 0.1.1

- Renamed the extension to `XASM Toolkit` to avoid a Marketplace display name conflict.
- Updated the extension description to better reflect its current feature set.

## 0.1.0

- First public release for the Visual Studio Marketplace.
- Published under the `seban-slt` publisher ID.
- Added Marketplace metadata and extension links.
- Added the `Snippets` Marketplace category.
- Added this changelog.
- Reduced the VSIX package size by excluding an unused image asset.

## 0.0.21

- Added syntax highlighting for the XASM `ALN` directive.
- Added 9 new XASM snippets.
- Expanded the snippet library to 14 reusable routines.
- Improved Atari800 launching on Linux.
- Fixed long-running pre-launch tasks so VS Code no longer waits indefinitely.
- Preserved Atari800 integrated terminal access for the built-in monitor.

## 0.0.20

- Improved Atari800 integration on Linux.
- Fixed terminal handling so the Atari800 monitor remains available.

## 0.0.19

- Added the `XASM: Initialize Project` command.
- Added project templates for build, run and editor configuration.

## 0.0.18

- Added the XASM snippet build system.
- Added generated VS Code snippets from normal `.xsm` source files.

