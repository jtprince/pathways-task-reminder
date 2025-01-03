from pathlib import Path
import subprocess


def to_image_path(inpath: Path, outpath: Path):
    # html_to_image = Html2Image(output_path=str(outpath.parent), size=(400, 200))
    # html_to_image.screenshot(html_file=str(inpath), save_as=outpath.name)
    # return outpath

    cmd = [
        "wkhtmltoimage",
        "--width",
        str(380),
        "--format",
        outpath.suffix[1:],
        str(inpath),
        str(outpath),
    ]
    subprocess.run(cmd)
    assert outpath.exists()
    return outpath
