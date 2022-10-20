
<script setup lang="ts">
// TODO: APIから取得する
import { ref } from 'vue'
const text_Id = ref('')
const text_Pw = ref('')
const myIcon = 'src/assets/logo.svg'
function IdInput(e) {
  text_Id.value = e.target.value
}
function PwInput(e) {
  text_Pw.value = e.target.value
}
//function Login()
//function SignUp()
</script>

<template>
  <main>
    <h1>ログイン</h1>
    <img
      :src="myIcon"
      alt="My photo（仮）"
      width="250"
    />
    <input :value="text_Id" @input="IdInput" placeholder="Your ID">
    <input type="password" :value="text_Pw" @input="PwInput" placeholder="Your Password">
    <button style="background: orange">Login</button>
    <item>
      <button>Sign up</button>
    </item>
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
