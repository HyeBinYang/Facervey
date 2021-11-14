<template>
  <div style="height: 100%;">
    <div :style="{ background: tmpData.survey.color }" style="height: 100%; padding-top: 50px; padding-bottom: 50px;">
      <div v-if="!isComplete">
        <div v-if="!isPossible">
          <v-card class="container" style="border-radius: 14px;">
            <h1 class="mb-5">
              응답 대상이 아닙니다.
            </h1>
          </v-card>
        </div>
        <div v-else-if="isSubmit">
          <v-card class="container" style="border-radius: 14px;">
            <h1 class="mb-5">
              이미 응답 하셨습니다.
            </h1>
          </v-card>
        </div>
        <div v-else>
          <v-card class="container" style="border-radius: 14px;">
            <h1 class="mb-5">
              {{ tmpData.survey.title }}
            </h1>
            <div>
              {{ tmpData.survey.description }}
            </div>
          </v-card>
          <v-card v-for="(question, index) in tmpData.questions" :key="question.pk" class="container mb-5" style="border-radius: 14px;">
            <div class="mb-5">
              {{ question.content }}
            </div>
            <div v-if="question.q_type === '객관식'">
              <v-radio-group v-model="answerForm.questions[index].answer">
                <div v-for="option in tmpData.answers" :key="option.pk" class="">
                  <v-radio v-show="option.q_pk === question.pk" :label="option.content" :value="option.pk" class="mb-2"></v-radio>
                </div>
              </v-radio-group>
            </div>
            <div v-else-if="question.q_type === '서술형'">
              <v-textarea
                outlined
                v-model="answerForm.questions[index].answer"
                name="input-7-4"
                label="작성해주세요"
              ></v-textarea>
            </div>
          </v-card>
          <div class="container text-right submit-btn">
            <button @click="submitAnswer(answerForm) + goComplete()" class="btn btn-success">제출</button>
          </div>
        </div>
      </div>
      <div v-else>
        <v-card class="container" style="border-radius: 14px;">
          <h1 class="mb-5">
            설문해주셔서 감사합니다.
          </h1>
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  methods: {
    ...mapActions(['submitAnswer', 'getStudents']),
    goComplete() {
      this.isComplete = true
    },
  },
  computed: {
    ...mapState(['Students', 'studentData', 'tmpData', 'answerData'])
  },
  created() {
    this.getStudents()
    this.answerForm.s_pk = this.tmpData.survey.pk
    this.answerForm.st_pk = this.studentData.pk
    this.tmpData.questions.forEach(question => {
      this.answerForm.questions.push({
        q_pk: question.pk,
        answer: null,
       })
    });
    this.questionNum = this.tmpData.questions.length
    if(this.answerData) {
      this.answerData.forEach(answer => {
          if(this.studentData.pk === answer.st_pk) {
            this.isSubmit = true
          }
      });
    }
  },
  mounted() {
    const SHA224 = require("sha224")
    Object.values(this.Students).forEach(student => {
      const buffer = SHA224(student.s_num)
      if(buffer.toString("hex") === this.$route.query.s_num) {
        this.isPossible = true
      }
    });
  },
  updated() {
    this.answerForm.st_pk = this.studentData.pk
  },
  data() {
    return {
      myUrl: '',
      isSubmit: false,
      isComplete: false,
      isPossible: false,
      questionNum: 0,
      radioGroup: 1,
      myname: this.$route.query.name,
      pk: this.$route.query.s_pk,
      answerForm: {
        st_pk: null,
        s_pk: null,
        questions: [],
      }
    }
  },
};
</script>

<style>
.navv {
  height: 100px;
  z-index: 1;
  top: -48px;
  position: fixed;
  background: #38393d;
  width: 100%;
}

@media screen and (max-width: 960px) {
       .submit-btn {
          margin-right: 0;
       }
}
</style>