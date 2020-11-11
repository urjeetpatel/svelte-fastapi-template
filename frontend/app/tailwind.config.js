module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [
    './src/**/*.html',
    './src/**/*.svelte',],
  theme: {
    extend: {
      colors: {
        primary: '#ff3e00'
      }
    },
  },
  variants: {},
  plugins: [],
}
