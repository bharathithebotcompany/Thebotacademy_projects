import Upload from "../components/Upload";
import ChatBox from "../components/ChatBox";

function Home() {
  return (
    <div className="max-w-3xl mx-auto mt-10 px-4">
      <h1 className="text-2xl font-bold mb-4 text-center">
        RAG AI Assistant
      </h1>

      {/* Upload PDF */}
      <Upload />

      {/* Chat section */}
      <div className="mt-6">
        <ChatBox />
      </div>
    </div>
  );
}

export default Home;
