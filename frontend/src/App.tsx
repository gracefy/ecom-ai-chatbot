import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "@/pages/home/HomePage";
import ProductDetailPage from "@/pages/product/[id]";
import Layout from "@/layout/Layout";

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/product/:id" element={<ProductDetailPage />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
