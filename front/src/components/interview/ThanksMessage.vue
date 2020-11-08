<template>
  <v-card>
    <img class='logo' src="../../assets/img/main/logo.png" alt="">
    <h4 class='head'>AI 모의 면접 서비스</h4>
    <div class="row justify-content-around message">
      <div class="col-lg-5 message-each">
        <h4 class='step'>STEP 1</h4>
        <img src="../../assets/img/interview/cart.png" alt="" class='message-icon'>
        <h6>원하시는 카테고리 내의 면접 질문들을 선택하세요.</h6>
      </div>
      <div class="col-lg-5 message-each">
        <h4 class='step'>STEP 2</h4>
        <img src="../../assets/img/interview/select.png" alt="" class='message-icon p-2'>
        <h6>선택된 질문들의 내용을 다시 한 번 확인한 후 최종 선택하세요.</h6>
      </div>
      <div class="col-lg-5 message-each">
        <h4 class='step'>STEP 3</h4>
        <img src="../../assets/img/interview/computer.png" alt="" class='message-icon'>
        <h6>더 단정하고 깔끔한 화면이 구성될 수 있도록 카메라를 조정하세요.</h6>
      </div>
      <div class="col-lg-5 message-each">
        <h4 class='step'>STEP 4</h4>
        <img src="../../assets/img/interview/start.png" alt="" class='message-icon'>
        <h6>시작하기 버튼을 누르시면 5초 후 면접이 자동으로 시작됩니다!</h6>
      </div>
    </div>
    <button class='btn btn-primary mb-4' @click="$router.push('/ready')">서비스 시작</button>
  </v-card>
</template>

<script>
export default {

}
</script>

<style scoped>
.head {
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  background-color: #64B5F6;
  height: 2rem;
  width: 240px;
  margin: auto;
  margin-top: 10px;
}
.logo {
  width: 300px;
  margin-top: 30px;
}
.message-icon {
  height: 150px;
  margin-bottom: 10px;
}
.step {
  margin: auto;
  color: white;
  background-color: black;
  width: 130px;
}
.message {
  padding: 20px 40px;
}
.message-each {
  margin: 10px 0px ;
}
</style>