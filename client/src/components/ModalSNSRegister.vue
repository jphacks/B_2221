<script setup lang="ts">
import { computed, ref, onMounted } from 'vue'

const dialog = ref<HTMLDialogElement | null>(null)
onMounted(() => {
  dialog.value?.showModal()
})
const emit = defineEmits(['close'])
function register() {
  // TODO: ここで登録処理を実装する
  dialog.value?.close()
  emit('close')
}
function cancel() {
  dialog.value?.close()
  emit('close')
}

const accountType = ref('email')
const inputTitle = computed(() => {
  switch (accountType.value) {
    case 'email':
      return 'メールアドレス'
    case 'facebook': // https://www.facebook.com/help/1740158369563165/?helpref=hc_fnav
      return 'FacebookユーザーID（ページID）'
    case 'github': // https://docs.github.com/ja/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-personal-account-settings/changing-your-github-username
      return 'GitHubアカウントID'
    case 'instagram': // https://www.facebook.com/help/instagram/369207764224422
      return 'Instagram ID（ユーザーネーム）'
    case 'line': // https://guide.line.me/ja/account-and-settings/account-and-profile/set-line-id.html
      return 'LINE ID'
    case 'linkedin': // https://www.linkedin.com/help/linkedin/answer/a522735?lang=ja
      return '公開プロフィールURL'
    case 'qiita': // https://help.qiita.com/ja/articles/qiita-change-id
      return 'ユーザ名'
    case 'tiktok': // https://support.tiktok.com/ja/getting-started/setting-up-your-profile/changing-your-username
      return 'TikTok ID（ユーザー名）'
    case 'twitter': // https://help.twitter.com/ja/managing-your-account/change-twitter-handle
      return 'Twitter ID（ユーザー名）'
    case 'wantedly': // https://help.wantedly.com/hc/ja/articles/9865050213913-プロフィール用のURLを設定したい
      return 'プロフィールURL'
    case 'website':
      return 'URL'
    case 'youtube': // https://support.google.com/youtube/answer/3250431?hl=ja
      return 'チャンネルID'
    case 'zenn': // https://zenn.dev/faq
      return 'Zenn ID（ユーザー名）'
    default:
      return 'アカウントID'
  }
})
const inputPrefix = computed(() => {
  switch (accountType.value) {
    case 'email':
      return ''
    case 'facebook':
      return 'https://www.facebook.com/'
    case 'github':
      return '@'
    case 'instagram':
      return '@'
    case 'line':
      return '@'
    case 'linkedin':
      return 'https://www.linkedin.com/in/'
    case 'qiita':
      return '@'
    case 'tiktok':
      return '@'
    case 'twitter':
      return '@'
    case 'wantedly':
      return 'https://www.wantedly.com/users/'
    case 'website':
      return 'https://'
    case 'youtube':
      return 'https://www.youtube.com/channel/'
    case 'zenn':
      return '@'
    default:
      return ''
  }
})
const inputType = computed(() => {
  switch (accountType.value) {
    case 'email':
      return 'email'
    case 'website':
      return 'url'
    default:
      return 'text'
  }
})

const accountID = ref('')
</script>

<template>
  <Teleport to="body">
    <dialog ref="dialog">
      <form method="dialog">
        <label>
          SNSタイプ:
          <select v-model="accountType">
            <option
              disabled
              value=""
            >
              選んでね
            </option>
            <option value="email">Email</option>
            <option value="facebook">Facebook</option>
            <option value="github">GitHub</option>
            <option value="instagram">Instagram</option>
            <option value="line">LINE</option>
            <option value="linkedin">LinkedIn</option>
            <option value="qiita">Qiita</option>
            <option value="tiktok">TikTok</option>
            <option value="twitter">Twitter</option>
            <option value="wantedly">Wantedly</option>
            <option value="website">Website</option>
            <option value="youtube">YouTube</option>
            <option value="zenn">Zenn</option>
          </select>
        </label>
        <label>
          {{ inputTitle }}:
          <span>
            {{ inputPrefix }}
            <input
              v-model="accountID"
              :type="inputType"
            />
          </span>
        </label>
        <menu>
          <button
            type="submit"
            @click="register"
          >
            登録する
          </button>
          <button
            type="reset"
            @click="cancel"
          >
            キャンセル
          </button>
        </menu>
      </form>
    </dialog>
  </Teleport>
</template>

<style scoped>
dialog {
  width: 100%;
  font-size: 1.5rem;
  padding: 1.5rem;
  margin: auto;
  border: 1px solid var(--color-border);
  border-radius: 0.5rem;
  box-shadow: 0 0 1rem rgba(0, 0, 0, 0.5);
}
dialog::backdrop {
  background-color: var(--color-background-mute);
}
dialog[open] {
  animation: bottom-up 1s ease-out;
}

form {
  display: grid;
  grid-template-columns: 1fr;
}
label {
  display: inline-block;
  margin-bottom: 1rem;
}
select {
  font-size: 1.5rem;
  border: 1px solid var(--color-border);
}
option {
  background-color: var(--color-background);
  border: 1px 0px solid var(--color-border);
}
input {
  font-size: 1.5rem;
  border: none;
}
button {
  font-size: 1.5rem;
  border: 1px solid var(--color-border);
  border-radius: 0.5rem;
  background-color: var(--color-background);
  color: var(--color-text);
  padding: 0.5rem 1rem;
  margin: 0.5rem;
}

@media (min-width: 768px) {
  dialog {
    width: 50%;
  }
}

@keyframes bottom-up {
  0% {
    transform: translateY(100%);
  }
  100% {
    transform: translateY(0);
  }
}
</style>
