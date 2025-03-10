module.exports = {
  darkMode: 'class', // Enable dark mode using the class strategy
  content: [
    './templates/**/*.html', // Adjust this path based on your project structure
    './static/**/*.js',      // If you have JavaScript files that use Tailwind classes
  ],
  theme: {
    extend: {
      colors: {
        'dark-gray': '#111111', // Custom dark gray color
        'light-gray': '#f0f0f0', // Custom light gray color
        'cs-blue' : '#7D9EA0',
        'cs-green' : '#A6A95E',
        'steel' : '#EBEEF6',
        'steel-dim' : '#C9CCD4',
      },
    },
  },
  plugins: [],
};
