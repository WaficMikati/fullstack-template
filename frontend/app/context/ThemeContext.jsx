import { createContext, useContext, useEffect, useState } from 'react'

const ThemeContext = createContext()

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('dark')

  // useEffect(() => {
  //   const savedTheme = localStorage.getItem('theme') || 'dark'
  //   setTheme(savedTheme)
  //   document.documentElement.setAttribute('data-bs-theme', savedTheme)
  // }, [])

  // useEffect(() => {
  //   document.documentElement.setAttribute('data-bs-theme', theme)
  //   localStorage.setItem('theme', theme)
  // }, [theme])

  const toggleTheme = () => {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'))
  }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

export function useTheme() {
  return useContext(ThemeContext)
}
