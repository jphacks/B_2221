/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

/** @type {import('eslint').Linter.Config} */
module.exports = {
  root: true,
  ignorePatterns: ['.git/*', 'node_modules/*', 'dist/*'],
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
    '@vue/eslint-config-typescript/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:@typescript-eslint/strict',
    '@vue/eslint-config-prettier',
  ],
  rules: {
    // use "@/*" instead
    'no-restricted-imports': ['error', { patterns: ['src/*', '../*'] }],

    '@typescript-eslint/consistent-type-imports': [
      'error',
      { prefer: 'type-imports', disallowTypeAnnotations: true },
    ],
    '@typescript-eslint/no-unsafe-argument': 'off',
    '@typescript-eslint/no-unsafe-assignment': 'off',
  },
  overrides: [
    {
      files: ['cypress/e2e/**.{cy,spec}.ts'],
      extends: ['plugin:cypress/recommended'],
    },
    {
      files: ['**/__tests__/**/*.{spec,test}.ts'],
      rules: {
        'no-restricted-imports': ['error', { patterns: ['src/*', '../../'] }],
      },
    },
  ],
  parser: 'vue-eslint-parser',
  parserOptions: {
    ecmaFeatures: { impliedStrict: true, jsx: false },
    ecmaVersion: 'latest',
    parser: '@typescript-eslint/parser',
    project: [
      './tsconfig.config.json',
      './tsconfig.app.json',
      './tsconfig.vitest.json',
      './tsconfig.json',
      './tsconfig.eslint.json',
    ],
    vueFeatures: { filter: false },
  },
}
