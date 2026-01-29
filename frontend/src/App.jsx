import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Home from "./components/Home"
import Login from "./components/Login"
import Register from "./components/Register"
import History from "./components/History"
import Playback from "./components/Playback"
import Upload from "./components/Upload"
import Results from "./components/Results"

export default function App(){
  return(
    <Router>
      <Routes>
        <Route path="/" element= {<Home/>} />
        <Route path="/login" element= {<Login/>} />
        <Route path="/register" element= {<Register/>} />
        <Route path="/history" element= {<History/>} />
        <Route path="/playback" element= {<Playback/>} />
        <Route path="/results" element= {<Results/>} />
        <Route path="/upload" element= {<Upload/>} />
      </Routes>
    </Router>
  )
}