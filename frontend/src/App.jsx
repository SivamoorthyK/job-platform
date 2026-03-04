import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import Jobs from './pages/Jobs'
import Applications from './pages/Applications'
import Analytics from './pages/Analytics'

function Navbar() {
  return (
    <nav className="bg-indigo-600 text-white px-6 py-3 flex gap-6">
      <Link to="/" className="font-bold text-lg">JobPlatform</Link>
      <Link to="/jobs" className="hover:underline">Jobs</Link>
      <Link to="/applications" className="hover:underline">Applications</Link>
      <Link to="/analytics" className="hover:underline">Analytics</Link>
    </nav>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/jobs" element={<Jobs />} />
        <Route path="/applications" element={<Applications />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </BrowserRouter>
  )
}