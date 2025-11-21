/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./frontend/**/*.{html,js}"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'board-white': '#f0d9b5',
        'board-black': '#b58863',
        'board-darker-black': '#5d4037',
      },
    },
  },
  plugins: [],
}
