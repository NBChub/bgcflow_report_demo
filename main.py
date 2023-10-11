
import json
import pandas as pd
from pathlib import Path

class Dict2Class(object):

    def __init__(self, my_dict):

        for key in my_dict:
            setattr(self, key, my_dict[key])

    def print_references(self):
        text = ""
        for r in self.references:
          text = "\n".join([text, f"- {r}"])
        return text

    def file_server(self):
        return "http://localhost:8002"

    def dependency_version(self):
        dependency_versions_path = Path(__file__).parent / "metadata/dependency_versions.json"
        if dependency_versions_path.is_file():
            with open(dependency_versions_path, "r") as f:
                dependency_versions = json.load(f)
                return dependency_versions["antismash"]
        else:
            print("WARNING: Unable to find dependency_versions.json file. Are you using BGCFlow >= 0.7.1?")
            print("WARNING: Assuming antismash version as 6.1.1")
            return "6.1.1"

def define_env(env):
  "Hook function"

  @env.macro
  def project():
      with open(Path(__file__).parent / "metadata/project_metadata.json", "r") as f:
          project_metadata = json.load(f)
          p = list(project_metadata.values())[0]
          p['name'] = [i for i in project_metadata.keys()][0]
          p = Dict2Class(p)
      return p

  @env.macro
  def read_csv_html(f, as_path):
    df = pd.read_csv(f)
    df = df.loc[:, ["genome_id", "source", "strain"]]
    for i in df.index:
        gid = df.loc[i, 'genome_id']
        df.loc[i, "url"] = f"<a href='{as_path}/{gid}/'>link</a>"
    html = df.to_html(table_id="myTable",
                      classes=["display"],
                      render_links=True,
                      escape=False).replace('border="1"','').replace('dataframe ', '')
    return html