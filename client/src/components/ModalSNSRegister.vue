<script setup lang="ts">
import { computed, ref } from 'vue'

const props = withDefaults(
  defineProps<{
    isOpen: boolean
  }>(),
  {
    isOpen: false,
  }
)
const emit = defineEmits(['close'])
function register() {
  // TODO: ここで登録処理を実装する
  emit('close')
}
function cancel() {
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
      return 'mailto:'
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
</script>

<template>
  <Teleport to="body">
    <dialog :open="isOpen">
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
          <span>{{ inputPrefix }}</span>
          <input type="text" />
        </label>
        <menu>
          <button
            type="submit"
            @click="register"
          >
            登録
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
