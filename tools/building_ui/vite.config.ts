import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
const backend = {
  target: "http://127.0.0.1:8792",
  changeOrigin: true,
  headers: { Origin: "http://127.0.0.1:8792" },
};
export default defineConfig({
  plugins: [react(), tailwindcss()],
  build: {
    outDir: "dist",
    assetsDir: "ui-assets",
    rollupOptions: {
      output: {
        manualChunks: { geometry: ["three"], react: ["react", "react-dom"] },
      },
    },
  },
  server: {
    port: 5174,
    proxy: {
      "/api": backend,
      "/assets": backend,
      "/library-assets": backend,
      "/exports": backend,
    },
  },
});
