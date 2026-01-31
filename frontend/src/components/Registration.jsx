import { useState } from "react";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";

export default function Registration() {
  const [form, setForm] = useState({
    username: "",
    firstname: "",
    middlename: "",
    lastname: "",
    email: "",
    password: "",
  });

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Form submitted:", form);
  }

  return (
    <div className="min-h-screen w-full bg-linear-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center p-4">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="w-full max-w-xl"
      >
        <div className="bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl shadow-2xl p-8">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-white">Create Account</h1>
            <p className="text-slate-300 mt-2 text-sm">
              Register to get started with your account
            </p>
          </div>

          {/* Form */}
          <form onSubmit={handleSubmit} className="space-y-5">
            {/* Username */}
            <Input
              label="Username"
              name="username"
              value={form.username}
              onChange={handleChange}
              placeholder="Enter username"
            />

            {/* Name Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <Input
                label="First Name"
                name="firstname"
                value={form.firstname}
                onChange={handleChange}
                placeholder="First name"
              />
              <Input
                label="Middle Name"
                name="middlename"
                value={form.middlename}
                onChange={handleChange}
                placeholder="Middle name"
              />
            </div>

            <Input
              label="Last Name"
              name="lastname"
              value={form.lastname}
              onChange={handleChange}
              placeholder="Last name"
            />

            {/* Email */}
            <Input
              label="Email"
              name="email"
              type="email"
              value={form.email}
              onChange={handleChange}
              placeholder="you@example.com"
            />

            {/* Password */}
            <Input
              label="Password"
              name="password"
              type="password"
              value={form.password}
              onChange={handleChange}
              placeholder="Enter password"
            />

            {/* Button */}
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              type="submit"
              className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-3 rounded-xl shadow-lg transition"
            >
              Create Account
            </motion.button>
          </form>

          {/* Footer */}
          <p className="text-center text-slate-300 text-sm mt-6">
            Already have an account? 
            <Link to = "/auth/login" className="text-indigo-400 hover:text-indigo-300 cursor-pointer ml-1">
              Login
            </Link>
          </p>
        </div>
      </motion.div>
    </div>
  );
}

function Input({ label, name, type = "text", value, onChange, placeholder }) {
  return (
    <div className="space-y-2">
      <label className="text-sm text-slate-200 font-medium">{label}</label>
      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        required
        className="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/20 text-white placeholder-slate-400 outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition"
      />
    </div>
  );
}
