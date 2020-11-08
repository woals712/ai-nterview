<template>
  <v-card
    class="mx-auto category"
    max-height="650"
    tile
  >
    <v-list shaped>
      <v-list-group
        v-for="item in items"
        :key="item.title"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="item.title"></v-list-item-title>
          </v-list-item-content>
        </template>
        
        <v-list-item-group color="primary">
          <v-list-item
            v-for="subItem in item.items"
            :key="subItem.title"
            @click='submitQuestionState(subItem.state)'
          >
            <v-list-item-content>
              <div class='d-flex'>
                <!-- <i class="fas fa-circle" style='padding-left:20px; font-size:1px;'></i> -->
                <v-list-item-title v-text="subItem.title"></v-list-item-title>

              </div>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>

      </v-list-group>
    </v-list>
  </v-card>
</template>

<script>
  export default {
    data() {
      return {
        state: 'vision',
        items: [
          {
            title: '성격별 면접 질문',
            items: [
              { title: '비전/목표', questionNumber:1, state:'vision' },
              { title: '조직적응력', questionNumber:2, state:'adaptation' },
              { title: '관심사/가치관', questionNumber:3, state:'values' },
              { title: '돌발/창의성', questionNumber:4, state:'creativity' },
              { title: '압박질문', questionNumber:5, state:'press' },
              { title: '기업/직무 적합도 및 관심도', questionNumber:6, state:'fitness' },
              { title: '대외활동 및 성격', questionNumber:7, state:'external' },
            ],
          },
          {
            title: '기업별 면접 질문',
            items: [
              { title: '넥슨', questionNumber:8, state:"nexon" },
              { title: 'LG전자', questionNumber:9, state:"lg" },
              { title: 'CJ 프레시웨이', questionNumber:10, state:"cj-fresh" },
              { title: 'CJ 올리브네트웍스', questionNumber:11, state:"cj-olive" },
              { title: 'CJ E&M', questionNumber:12, state:"cj-enm" },
              { title: 'CJ 대한통운', questionNumber:13, state:"cj-daehan" },
              { title: '삼성전자', questionNumber:14, state:"samsung" },
              { title: '신한은행', questionNumber:15, state:"sinhan" },
              { title: '하나은행', questionNumber:16, state:"keb" },
              { title: '한국전력', questionNumber:17, state:"ke" },
              { title: 'LH 토지주택공사', questionNumber:18, state:"lh" },
              { title: '현대백화점', questionNumber:19, state:"hd-dep" },
              { title: '현대모비스', questionNumber:20, state:"hd-mobis" },
              { title: 'SK하이닉스', questionNumber:21, state:"sk" },
            ],
          },
          {
            title: '직무별 면접 질문',
            items: [
              { title: 'IT/인터넷', questionNumber:22, state:"it" },
              { title: '디자인', questionNumber:23, state:"design" },
              { title: '마케팅/시장조사', questionNumber:24, state:"marketing" },
              { title: '경영/기획/컨설팅', questionNumber:25, state:"business" },
              { title: '미디어/홍보직', questionNumber:26, state:"media" },
              { title: '기타', questionNumber:27, state:"etc" },
            ],
          },
          {
            title: '내 면접 질문',
            items: [
              { title: '질문 만들기', questionNumber:28, state:"newQuestion" },
              { title: '내 질문', questionNumber: 29, state:this.$store.getters.getUsername },
            ],
          },
        ],
      }
    },
    methods: {
      submitQuestionState(state) {
        this.state = state
        this.$emit('submit-question-state', this.state)
      }
    },
  }
</script>

<style>
.category {
  overflow:auto;
}
</style>