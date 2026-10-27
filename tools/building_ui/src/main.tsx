import { createRoot } from "react-dom/client";
import App from "./App";
import { createEditorStore } from "./store";
import "./styles.css";
createRoot(document.getElementById("root")!).render(
  <App store={createEditorStore()} />,
);
