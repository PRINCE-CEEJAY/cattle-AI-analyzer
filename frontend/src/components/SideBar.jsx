import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Menu, X, UserPlus, LogIn, LayoutDashboard, BookOpenText, LogOutIcon } from "lucide-react";
import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {
  const [open, setOpen] = useState(true);
  const location = useLocation();

  const links = [
    { name: "Dashboard", to: "/history", icon: LayoutDashboard },
    { name: "Results", to: "/results", icon: BookOpenText },
    { name: "Register", to: "/auth/registration", icon: UserPlus },
    { name: "Login", to: "/auth/login", icon: LogIn },
    { name: "Logout", to: "/auth/logout", icon: LogOutIcon },
  ];

  return (
    <>
      {/* Toggle Button */}
      <button
        onClick={() => setOpen((p) => !p)}
        className="fixed top-4 left-4 z-50 p-2 rounded-xl bg-slate-900 text-white shadow-lg hover:scale-105 transition"
      >
        {open ? <X size={22} /> : <Menu size={22} />}
      </button>

      {/* Sidebar */}
      <AnimatePresence>
        {open && (
          <motion.aside
            initial={{ x: -260, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: -260, opacity: 0 }}
            transition={{ duration: 0.25 }}
            className="fixed top-0 left-0 h-screen w-64 bg-slate-900 border-r border-slate-800 shadow-2xl p-6 flex flex-col"
          >
            {/* Header */}
            <div className="mb-10 mx-auto">             
              <p className=" text-slate-400 text-md font-bold mt-1">Menu</p>
            </div>

            {/* Links */}
            <nav className="flex flex-col gap-2">
              {links.map((item) => {
                const Icon = item.icon;
                const active = location.pathname === item.to;

                return (
                  <Link
                    key={item.to}
                    to={item.to}
                    className={`flex items-center gap-3 px-4 py-3 rounded-xl transition group
                      ${
                        active
                          ? "bg-indigo-600 text-white shadow-lg"
                          : "text-slate-300 hover:bg-slate-800 hover:text-white"
                      }`}
                  >
                    <Icon size={18} />
                    <span className="font-medium">{item.name}</span>
                  </Link>
                );
              })}
            </nav>

            {/* Footer */}
            <div className="mt-auto pt-6 border-t border-slate-800">
              <div className="text-xs text-slate-500">
                © {new Date().getFullYear()} Ceejay Dev
              </div>
            </div>
          </motion.aside>
        )}
      </AnimatePresence>
    </>
  );
}
