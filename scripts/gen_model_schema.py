import argparse
import json
from pathlib import Path
from typing import Union

from pydantic import BaseModel, TypeAdapter

from template import model

THIS_DIR = Path(__file__).absolute().parent
DEFAULT_OUTPUT_FILE = THIS_DIR.parent / "model.schema.json"


def gen_model_schema(output_file: Path):
    all_model_types = tuple(
        cls
        for cls in model.__dict__.values()
        if isinstance(cls, type) and cls != BaseModel and issubclass(cls, BaseModel)
    )
    ta = TypeAdapter(Union[all_model_types])
    output_file.write_text(json.dumps(ta.json_schema(), indent=2) + "\n")
    print(f"Wrote {[t.__name__ for t in all_model_types]} to {output_file}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-file", type=Path, default=DEFAULT_OUTPUT_FILE)
    args = parser.parse_args()

    gen_model_schema(args.output_file)


if __name__ == "__main__":
    main()
