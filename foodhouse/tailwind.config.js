/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./src/**/*.{html,js,py}'],
    theme: {
      extend: {
        colors: {
          primary: '#E8AA42',
          secondary: '#025464',
          accent: '#E57C23',
          text: '#0F1B1F',
          background: '#F7F7F7',
        },
        screens: {
          xs: '370px',
          sm: '540px',
          md: '768px',
          lg: '1024px',
          xl: '1280px',
          xxl: '1440px',
        },
        fontFamily: {
          text: ['Poppins', 'sans-serif'],
          title: ['Rubik', 'sans-serif'],
          logo: ['Lumanosimo', 'cursive'],
        },
        gridTemplateRows: {
          12: 'repeat(12, minmax(0, 1fr))',
        },
      },
    },
    plugins: [require('tailwind-scrollbar')],
  };