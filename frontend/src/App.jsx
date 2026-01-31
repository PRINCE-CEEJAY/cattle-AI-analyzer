import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Home from "./components/Home"
import Login from "./components/Login"
import Registration from "./components/Registration"
import History from "./components/History"
import Upload from "./components/Upload"
import Results from "./components/Results"
import Dashboard from "./components/Dashboard"


export default function App(){
  return(  
      <Routes>
        <Route path="/" element= {<Home/>} />
        <Route path="/auth/registration" element= {<Registration/>} />
        <Route path="/auth/login" element= {<Login/>} />
        <Route path="/upload" element= {<Upload/>} />
        <Route path="/dashboard" element= {<Dashboard/>} />       
        <Route path="/results" element= {<Results/>} />
        <Route path="/history" element= {<History/>} />       
      </Routes>
  )
}