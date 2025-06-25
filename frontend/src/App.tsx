import "./App.css";
import Chatbot from "@/features/Chatbot";

function App() {
  return (
    <div className="bg-[url(/home-bg.jpg)] min-h-screen w-full bg-cover bg-center bg-no-repeat">
      <div className="absolute inset-0 bg-black/20 z-10">
        <div className="z-50">
          <Chatbot />
        </div>
      </div>
    </div>
  );
}

export default App;
