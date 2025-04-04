import subprocess


def replaceInDocument(FIO: str, dateTill: str, pdfFileName: str) -> None:
    with open("certificate.svg", "r", encoding="utf-8") as file:
        svg_content = file.read()
    svg_content = svg_content.replace("fioHandler", FIO)
    svg_content = svg_content.replace("dateHandler", dateTill)

    temp_svg_path = "temp_certificate.svg"
    with open(temp_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    subprocess.run([
        "inkscape",
        temp_svg_path,
        "--export-type=pdf",
        f"--export-filename={pdfFileName}"
    ], check=True)

    print(f"PDF успешно создан: {pdfFileName}")
