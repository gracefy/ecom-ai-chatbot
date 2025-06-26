function HomePage() {
  return (
    <div className="flex flex-col items-center justify-center px-4 py-8 text-white space-y-8">
      <h1 className="text-5xl font-extrabold drop-shadow-lg text-center">
        Welcome to the AI Fashion Chatbot
      </h1>

      <div className="bg-white/10 backdrop-blur-md rounded-2xl p-6 max-w-2xl text-white shadow-lg space-y-4 font-sans">
        <p>
          This is a personal project exploring an AI-powered fashion Q&A
          chatbot. It uses OpenAI Embedding & Chat APIs, Azure AI Search, and
          fashion product data from{" "}
          <a
            href="https://www.kaggle.com/datasets/shivamb/fashion-clothing-products-catalog"
            target="_blank"
            rel="noopener noreferrer"
            className="underline text-blue-200 hover:text-blue-300"
          >
            this Kaggle dataset
          </a>
          .
        </p>
        <p className="font-semibold">Try asking things like:</p>
        <ul className="list-disc list-inside space-y-1">
          <li>“Show me red floral dresses under 5000 INR”</li>
          <li>“What is the difference between slim fit and regular fit?”</li>
          <li>“Do you have a summer outfit recommendation?”</li>
        </ul>
      </div>
    </div>
  );
}

export default HomePage;
