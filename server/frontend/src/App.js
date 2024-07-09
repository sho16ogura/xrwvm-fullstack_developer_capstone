import LoginPanel from "./components/Login/Login"
import 
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<LoginPanel />} />
    </Routes>
  );
}
export default App;
