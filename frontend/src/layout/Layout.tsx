import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Chatbot from "@/features/Chatbot";
import { motion } from "framer-motion";

const Layout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div
      className="relative flex flex-col min-h-screen bg-cover bg-center bg-no-repeat"
      style={{ backgroundImage: "url('/home-bg.jpg')" }}
    >
      <div className="absolute inset-0 bg-black/50 z-0"></div>
      <div className="relative flex flex-col min-h-screen z-10">
        <Header />

        <main className="flex-grow flex">{children}</main>

        <Footer />

        <motion.div
          initial={{ y: 0 }}
          animate={{ y: [0, -20, 0, -8, 0] }}
          transition={{
            duration: 1.6,
            ease: "easeInOut",
          }}
        >
          <Chatbot />
        </motion.div>
      </div>
    </div>
  );
};

export default Layout;
