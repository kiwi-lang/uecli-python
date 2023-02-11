import subprocess

import pytest

from uetools.core import args, main
from uetools.core.conf import ready

skipif = pytest.mark.skipif

# but it works if I build for Gamekit
#       - uecli plugin GamekitDev Plugins/Gamekit/Gamekit.uplugin --output E:/Trash --platform Win64
#
# ERROR: Environment variable 'CommonProgramFiles' is not defined (referenced by E:\UnrealEngine\Engine\Source\ThirdParty\ADO\ADO.Build.cs)


@skipif(True, reason="Failing on the example plugin")
@skipif(not ready(), reason="Unreal engine is not installed")
def test_plugin(project, project_name, tmp_path):

    main(
        args(
            "ubt",
            "build",
            "--target",
            f"{project_name}Editor",
            "--mode",
            "Development",
        )
    )

    main(
        args(
            "plugin",
            "package",
            project_name,
            "Plugins/ExamplePlugin/ExamplePlugin.uplugin",
            "--output",
            "E:/Trash",
            "--platforms",
            "Win64",
        )
    )

    print(subprocess.run(["ls"], cwd=project))
