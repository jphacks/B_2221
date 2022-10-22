<script setup lang="ts">
// TODO: APIから取得する
import { ref } from 'vue'
const textId = ref('')
const password = ref('')
//function Login()
//function SignUp()
</script>

<template>
  <main>
    <h1>ログイン</h1>
    <input
      v-model="textId"
      placeholder="Your ID"
    />
    <input
      v-model="password"
      type="password"
      placeholder="Your Password"
    />
    <button style="background: orange">Login</button>
    <a href="/signup">Sign up</a>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
input {
  font-size: 1rem;
  padding: 0.8rem;
  margin: 0.5rem;
  width: 250px;
  letter-spacing: 0.1rem;
}
button {
  font-size: 1rem;
  padding: 0.5rem;
  margin: 0.5rem;
  width: 250px;
  border-color: white;
  letter-spacing: 0.1rem;
}
</style>
