<script setup lang="ts">
</script>

<template>
    <main>
        <dev class="box1">
            <dev class="aa">
                <img class="take-photo" src="../../public\image\img_example.png">
            </dev>
            <button class="torikesu">取り消す</button>
        </dev>
        <dev class="box2">
        <img class="predict-photo" src="../../public\image\img_example.png">
        </dev>
        <dev class="box3">
            <button class="confirm">この人です</button>
            <button class="home">ホームへ</button>
        </dev>
    </main>
</template>


<script>

</script>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.box1{
    text-align : center ;
    width: 500px;
    height: 200px;
    top: 20px
}
.box2{
    top: 20px;
    text-align : center 
}
.box3{
    text-align : center ;
    width: 300px;
    height: 400px;
    top: 20px;
}
img.take-photo {
    width: 125px;
    height: 142px;
    right: 75px;
    top: 25px;
    border-radius: 15px;
}

img.predict-photo {
    width: 400px;
    height: 500px;
    top: 20px;
    border-radius: 15px;
}
button.confirm {
    width: 214px;
    height: 41px;
    top: 50px;
    border-radius: 15px;
}

button.home {
    width: 214px;
    height: 45px;
    top: 75px;
    border-radius: 15px;
}

button.torikesu {
    width: 125px;
    height: 55px;
    left: 50px;
    top: 0px;
    border-radius: 15px;
}
</style>