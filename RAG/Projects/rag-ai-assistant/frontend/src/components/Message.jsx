function Message({ role, text }) {
  return (
    <div className={`my-2 ${role === "user" ? "text-right" : "text-left"}`}>
      <span className="inline-block p-2 bg-gray-200 rounded">
        {text}
      </span>
    </div>
  );
}

export default Message;
