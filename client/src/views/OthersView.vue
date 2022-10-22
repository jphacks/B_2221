<script setup lang="ts">
// TODO: APIから取得する
const myIcon = 'src/assets/logo.svg'
const snsLists = [
  {
    type: 'github',
    icon: 'src/assets/icons/GitHub-Mark-120px-plus.png',
    userName: '@u-sho',
    url: 'https://github.com/u-sho',
  },
  {
    type: 'github',
    icon: 'src/assets/icons/GitHub-Mark-120px-plus.png',
    userName: '@u-sho',
    url: 'https://github.com/u-sho',
  },
]
</script>

<template>
  <main>
    <h1>ユーザーネーム</h1>
    <img
      :src="myIcon"
      alt="My photo（仮）"
      width="300"
    />
    <ul>
      <li
        v-for="sns in snsLists"
        :key="sns.url"
      >
        <a :href="sns.url">
          <img
            :src="sns.icon"
            :alt="sns.type + ' icon'"
            width="24"
          />
          {{ sns.userName }}
        </a>
      </li>
    </ul>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
ul {
  text-align: center;
  padding: 0 0 0 0;
}
li {
  list-style: none;
  height: 1.5rem;
  line-height: 1;
  font-size: 1.5rem;
  margin: 1.5rem 0;
}
</style>
