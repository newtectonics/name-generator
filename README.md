# name-generator
A silly little name generator to test flake deployment

# Usage as a flake

[![FlakeHub](https://img.shields.io/endpoint?url=https://flakehub.com/f/newtectonics/name-generator/badge)](https://flakehub.com/flake/newtectonics/name-generator)

Add name-generator to your `flake.nix`:

```nix
{
  inputs.name-generator.url = "https://flakehub.com/f/newtectonics/name-generator/*.tar.gz";

  outputs = { self, name-generator }: {
    # Use in your outputs
  };
}

```
