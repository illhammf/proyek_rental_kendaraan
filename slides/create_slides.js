const pptxgen = require('pptxgenjs');
const { warnIfSlideHasOverlaps, warnIfSlideElementsOutOfBounds } = require('/home/oai/skills/slides/pptxgenjs_helpers');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'ChatGPT';
pptx.subject = 'Sistem Rental Kendaraan OOP';
pptx.title = 'Sistem Rental Kendaraan OOP';
pptx.company = 'Tugas Bahasa Pemrograman';
pptx.lang = 'id-ID';
pptx.theme = {
  headFontFace: 'Aptos Display',
  bodyFontFace: 'Aptos',
  lang: 'id-ID',
};
pptx.defineLayout({ name: 'CUSTOM_WIDE', width: 13.333, height: 7.5 });
pptx.layout = 'CUSTOM_WIDE';

const C = {
  navy: '102A43', blue: '2F80ED', light: 'EEF5FF', white: 'FFFFFF', gray: '475569', green: '219653', orange: 'F2994A', line: 'CBD5E1', dark: '0F172A'
};

function addTitle(slide, title, subtitle='') {
  slide.background = { color: C.white };
  slide.addText(title, { x: 0.7, y: 0.35, w: 8.7, h: 0.45, fontFace: 'Aptos Display', fontSize: 24, bold: true, color: C.navy, margin: 0 });
  if (subtitle) slide.addText(subtitle, { x: 0.72, y: 0.88, w: 8.8, h: 0.25, fontSize: 10, color: C.gray, margin: 0 });
  slide.addShape(pptx.ShapeType.line, { x: 0.7, y: 1.18, w: 11.9, h: 0, line: { color: C.line, width: 1 } });
}
function addFooter(slide, n) {
  slide.addText(`Sistem Rental Kendaraan OOP | ${n}`, { x: 10.8, y: 7.1, w: 1.7, h: 0.2, fontSize: 8, color: '64748B', align: 'right', margin: 0 });
}
function bullet(slide, items, x, y, w, fs=15) {
  slide.addText(items.map(t => ({ text: t, options: { bullet: { indent: 14 }, hanging: 4, breakLine: true } })), {
    x, y, w, h: items.length*0.45 + 0.1, fontSize: fs, color: C.dark, fit: 'shrink', margin: 0.02, breakLine: false,
  });
}
function box(slide, text, x, y, w, h, fill=C.light, color=C.navy) {
  slide.addShape(pptx.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: { color: 'D6E4FF', width: 1 } });
  slide.addText(text, { x: x+0.12, y: y+0.12, w: w-0.24, h: h-0.24, fontSize: 13, color, bold: true, align: 'center', valign: 'mid', margin: 0.02, fit: 'shrink' });
}
function sectionLabel(slide, text, x, y, color=C.blue) {
  slide.addText(text, { x, y, w: 2.8, h: 0.3, fontSize: 10, bold: true, color, margin: 0 });
}

// Slide 1
{
  const s = pptx.addSlide();
  s.background = { color: C.navy };
  s.addText('Sistem Rental Kendaraan', { x: 0.75, y: 1.1, w: 7.4, h: 0.6, fontSize: 36, bold: true, color: C.white, margin: 0 });
  s.addText('Berbasis Object-Oriented Programming dengan Python', { x: 0.78, y: 1.85, w: 7.2, h: 0.32, fontSize: 17, color: 'D6E4FF', margin: 0 });
  s.addText('Tugas Bahasa Pemrograman', { x: 0.8, y: 2.45, w: 4, h: 0.35, fontSize: 13, color: C.white, margin: 0 });
  box(s, 'Python', 8.7, 1.25, 2.1, 0.75, 'EFF6FF');
  box(s, 'OOP', 10.95, 1.25, 1.55, 0.75, 'ECFDF5', C.green);
  box(s, 'CLI', 8.7, 2.25, 1.6, 0.75, 'FFF7ED', C.orange);
  box(s, 'JSON', 10.55, 2.25, 1.95, 0.75, 'F8FAFC');
  s.addText('Mobil, motor, pelanggan, transaksi, laporan.', { x: 0.82, y: 5.85, w: 7.6, h: 0.32, fontSize: 13, color: 'CBD5E1', margin: 0 });
  addFooter(s, 1);
}
// Slide 2
{
  const s = pptx.addSlide(); addTitle(s, 'Latar Belakang', 'Kebutuhan pencatatan rental kendaraan yang lebih rapi dan terstruktur.');
  bullet(s, ['Pencatatan manual rentan data ganda dan kehilangan arsip.', 'Status kendaraan perlu dipantau agar tidak terjadi double booking.', 'Transaksi rental membutuhkan perhitungan biaya yang konsisten.', 'Python OOP cocok karena entitas rental dapat dimodelkan sebagai class.'], 0.85, 1.65, 6.2, 15);
  box(s, 'Masalah\nData tidak rapi', 7.65, 1.55, 2.1, 1.25, 'FFF7ED', C.orange);
  box(s, 'Solusi\nAplikasi Python', 10.1, 1.55, 2.1, 1.25, 'EEF5FF', C.blue);
  box(s, 'Output\nLaporan TXT/CSV', 8.85, 3.3, 2.2, 1.25, 'ECFDF5', C.green);
  addFooter(s, 2);
}
// Slide 3
{
  const s = pptx.addSlide(); addTitle(s, 'Analisis Kebutuhan', 'Fungsi utama yang harus tersedia pada aplikasi.');
  sectionLabel(s, 'Kebutuhan Fungsional', 0.85, 1.45);
  bullet(s, ['Tambah dan lihat kendaraan.', 'Tambah dan lihat pelanggan.', 'Sewa dan kembalikan kendaraan.', 'Simpan data JSON dan buat laporan.'], 0.85, 1.8, 5.3, 14);
  sectionLabel(s, 'Kebutuhan Nonfungsional', 7.0, 1.45, C.green);
  bullet(s, ['Mudah dijalankan di VS Code.', 'Tidak membutuhkan library eksternal.', 'Kode diberi komentar belajar.', 'Struktur folder rapi dan modular.'], 7.0, 1.8, 5.3, 14);
  addFooter(s, 3);
}
// Slide 4
{
  const s = pptx.addSlide(); addTitle(s, 'Desain Class', 'Class utama sesuai konsep tugas.');
  const xs = [0.75, 3.1, 5.45, 7.8, 10.15];
  const names = ['Kendaraan', 'Mobil', 'Motor', 'Pelanggan', 'Transaksi'];
  names.forEach((name, i) => box(s, name, xs[i], 1.7, 1.85, 0.8, i===0?'EEF5FF':'F8FAFC'));
  box(s, 'Rental', 4.95, 4.0, 2.05, 0.85, 'ECFDF5', C.green);
  box(s, 'FileManager', 2.4, 5.35, 2.1, 0.7, 'FFF7ED', C.orange);
  box(s, 'Laporan', 7.45, 5.35, 1.8, 0.7, 'FFF7ED', C.orange);
  s.addText('Mobil dan Motor mewarisi Kendaraan. Rental menjadi pusat pengelolaan data.', { x: 1.0, y: 6.45, w: 10.8, h: 0.35, fontSize: 14, color: C.gray, align: 'center', margin: 0 });
  addFooter(s, 4);
}
// Slide 5
{
  const s = pptx.addSlide(); addTitle(s, 'Implementasi Konsep OOP', 'Pemetaan konsep ke bagian kode program.');
  box(s, 'Inheritance\nMobil dan Motor extends Kendaraan', 0.85, 1.45, 3.5, 1.15, 'EEF5FF');
  box(s, 'Encapsulation\nPrivate attribute + property', 4.9, 1.45, 3.5, 1.15, 'ECFDF5', C.green);
  box(s, 'Polymorphism\nOverride biaya dan info', 8.95, 1.45, 3.5, 1.15, 'FFF7ED', C.orange);
  box(s, 'Composition\nRental memiliki FileManager dan Laporan', 2.7, 3.55, 3.8, 1.15, 'F8FAFC');
  box(s, 'Constructor\nSetiap class memakai __init__()', 6.95, 3.55, 3.8, 1.15, 'F8FAFC');
  addFooter(s, 5);
}
// Slide 6
{
  const s = pptx.addSlide(); addTitle(s, 'Alur Program', 'Program berjalan melalui menu terminal.');
  const steps = ['Muat Data', 'Pilih Menu', 'Proses Method', 'Simpan Data', 'Laporan'];
  steps.forEach((step, i) => { box(s, step, 0.95 + i*2.35, 2.2, 1.75, 0.8, i%2===0?'EEF5FF':'F8FAFC'); });
  s.addText('Alur dibuat sederhana agar mudah didemonstrasikan saat presentasi.', { x: 1.5, y: 4.1, w: 10, h: 0.35, fontSize: 15, color: C.gray, align: 'center', margin: 0 });
  addFooter(s, 6);
}
// Slide 7
{
  const s = pptx.addSlide(); addTitle(s, 'Fitur Aplikasi', 'Fitur yang dapat dicoba langsung saat demo.');
  bullet(s, ['Data contoh otomatis dibuat saat program pertama dijalankan.', 'Pengguna dapat menambah mobil, motor, dan pelanggan.', 'Transaksi sewa menghitung total biaya otomatis.', 'Pengembalian mengubah status kendaraan menjadi tersedia.', 'Laporan dibuat dalam format TXT dan CSV.'], 0.9, 1.55, 6.4, 15);
  box(s, 'Menu CLI', 8.0, 1.75, 3.2, 0.9, 'EEF5FF');
  box(s, 'Data JSON', 8.0, 3.05, 3.2, 0.9, 'ECFDF5', C.green);
  box(s, 'Laporan', 8.0, 4.35, 3.2, 0.9, 'FFF7ED', C.orange);
  addFooter(s, 7);
}
// Slide 8
{
  const s = pptx.addSlide(); addTitle(s, 'Skenario Demo', 'Urutan demo singkat 10 menit.');
  bullet(s, ['Jalankan python main.py.', 'Tampilkan data kendaraan dan pelanggan.', 'Buat transaksi sewa kendaraan.', 'Tampilkan transaksi dan statistik.', 'Lakukan pengembalian kendaraan.', 'Buat laporan dan tunjukkan file reports.'], 1.0, 1.55, 7.1, 15);
  box(s, 'Target Demo\nSeluruh konsep OOP terlihat melalui fitur yang dijalankan.', 8.9, 2.25, 3.0, 1.5, 'F8FAFC');
  addFooter(s, 8);
}
// Slide 9
{
  const s = pptx.addSlide(); addTitle(s, 'Pengujian', 'Testing memastikan fitur utama berjalan.');
  box(s, '1\nTambah kendaraan', 0.85, 1.65, 2.0, 0.95, 'EEF5FF');
  box(s, '2\nTambah pelanggan', 3.2, 1.65, 2.0, 0.95, 'EEF5FF');
  box(s, '3\nPolymorphism biaya', 5.55, 1.65, 2.0, 0.95, 'ECFDF5', C.green);
  box(s, '4\nTransaksi kembali', 7.9, 1.65, 2.0, 0.95, 'ECFDF5', C.green);
  box(s, '5\nStatistik', 10.25, 1.65, 2.0, 0.95, 'FFF7ED', C.orange);
  s.addText('Jalankan: python tests/test_rental.py', { x: 2.2, y: 4.25, w: 8.8, h: 0.45, fontSize: 20, bold: true, color: C.navy, align: 'center', margin: 0 });
  addFooter(s, 9);
}
// Slide 10
{
  const s = pptx.addSlide(); addTitle(s, 'Kesimpulan', 'Aplikasi memenuhi kebutuhan dasar proyek OOP.');
  bullet(s, ['Sistem berhasil mengelola kendaraan, pelanggan, transaksi, dan laporan.', 'Konsep OOP diterapkan secara eksplisit dan mudah ditunjukkan.', 'Kode modular dan diberi komentar agar mudah dipelajari.', 'Proyek siap dijalankan dan dipresentasikan melalui VS Code.'], 1.0, 1.55, 7.4, 16);
  box(s, 'Siap Demo', 9.05, 2.2, 2.6, 1.15, 'ECFDF5', C.green);
  addFooter(s, 10);
}

for (const slide of pptx._slides) {
  warnIfSlideHasOverlaps(slide, pptx, { ignoreLines: true, ignoreDecorativeShapes: true });
  warnIfSlideElementsOutOfBounds(slide, pptx);
}

pptx.writeFile({ fileName: '/mnt/data/Sistem_Rental_Kendaraan_OOP/slides/Slide_Presentasi_Rental_Kendaraan_OOP.pptx' });
