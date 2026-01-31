import { Contact, HomeIcon, LayoutDashboardIcon, LogInIcon, Moon, NotebookPenIcon, Plus, BookOpenText, SeparatorVertical, Sun, LogOut, CircleUserRound, Menu } from "lucide-react"
import { Link } from "react-router-dom";
import { useState } from "react";

export default function SideBar() {
    const [visible, setVisible] = useState(true)

    const toggleSidebar = () => setVisible(prev=>!prev)

  const nav = [
    {
    id: 1,
    link: '/',
    icon: <HomeIcon/>,
    text: 'Home'
  },
    {
    id: 2,
    link: '/dashboard',
    icon: <LayoutDashboardIcon/>,
    text: 'Dashboard'
  },
    {
    id: 3,
    link: '/upload',
    icon: <Plus/>,
    text: 'Upload Video'
  },
    {
    id: 4,
    link: '/results',
    icon: <BookOpenText/>,
    text: 'Analysis Results'
  },
    {
    id: 5,
    link: '/history',
    icon: <Contact/>,
    text: 'History'
  },
]

  return (
    <div className="flex flex-col w-fit">  
        <div className="w-full text-right bg-transparent">
            <button className="font-extrabold cursor-pointer opacity-85 text-red-500  hover:opacity-100" onClick={toggleSidebar}> 
                <Menu/> 
            </button>      
        </div>     
        {
            visible && 
            <div className="flex flex-col lg:font-extrabold justify-evenly px-2 h-full  sidebar">
                {nav.map(({id, link, icon, text})=>( 
                    <div className="flex gap-1" key={id}>  
                    {icon}
                    <Link to= {link} className="">{text}</Link>
                    </div>
                    ))}
                <div className="flex gap-1 items-center">
                    <CircleUserRound/>
                    <button className="bg-orange-700 px-2 py-1 rounded-full hover:bg-orange-500 cursor-pointer">Logout</button>
                </div>

            </div>
        }
    </div>
  )
}
