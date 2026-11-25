import api from "../api/client";

function Upload() {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    await api.post("/upload", formData);
    alert("PDF uploaded successfully!");
  };

  return (
    <div className="p-4 border rounded">
      <input type="file" accept=".pdf" onChange={handleUpload} />
    </div>
  );
}

export default Upload;

