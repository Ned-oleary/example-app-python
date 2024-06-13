/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
    // Make sure these paths are correct and point to files that use Tailwind classes
  ],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
      'accent-primary': '#7a65fe',
      'cream1': '#f7f7f0',
      'gray1': '#e1e3e1',
      'gray2': '#d9d9d9',
      'mediumgray': '#918e8e',
      'mediumgray2': '#aba7a7',
      'white': '#ffffff',
      'blue': '#1fb6ff',
      'purple': '#7e5bef',
      'pink': '#ff49db',
      'orange': '#ff7849',
      'green': '#13ce66',
      'yellow': '#ffc82c',
      'gray-dark': '#273444',
      'gray': '#8492a6',
      'gray-light': '#f5f5f5',
      'gray-light2': 'f2f0f0',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      }
      
    }
  }
}