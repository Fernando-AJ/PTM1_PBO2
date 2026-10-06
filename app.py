from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


class Mahasiswa:
    """Merepresentasikan satu objek mahasiswa."""

    def __init__(self, nim, nama, prodi):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi

    def tampilkan_data(self):
        return f"{self.nim} - {self.nama} - {self.prodi}"


# Penyimpanan sementara di memori (belum menggunakan database)
data_mahasiswa = [
    Mahasiswa("20260001", "Budi Santoso", "Teknik Informatika"),
    Mahasiswa("20260002", "Siti Aminah", "Teknik Informatika"),
]


@app.route("/", methods=["GET", "POST"])
def index():
    pesan = None

    if request.method == "POST":
        nim = request.form.get("nim", "").strip()
        nama = request.form.get("nama", "").strip()
        prodi = request.form.get("prodi", "").strip()

        if not nim or not nama or not prodi:
            pesan = "Semua field wajib diisi."
        elif any(m.nim == nim for m in data_mahasiswa):
            pesan = "NIM sudah terdaftar."
        else:
            mahasiswa = Mahasiswa(nim, nama, prodi)
            data_mahasiswa.append(mahasiswa)
            return redirect(url_for("index"))

    return render_template("index.html", mahasiswa=data_mahasiswa, pesan=pesan)


@app.route("/hapus/<nim>", methods=["POST"])
def hapus(nim):
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m.nim != nim]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
