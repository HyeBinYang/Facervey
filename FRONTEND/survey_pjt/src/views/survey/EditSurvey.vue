<template>
  <div style="height: 100%">
    <Nav></Nav>
    <v-tabs
      fixed-tabs
      v-model="tab"
    >
      <v-tab 
        v-for="item in items"
        :key="item"
      >
          {{ item }}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab" style="height: 100%;">
      <v-tab-item
        v-for="item in items"
        :key="item"
        style="height: 100%;"
      >
        <div v-if="item === '설문'" :style="{ background: FormData.survey.color }" style="height: 100%; padding-top: 50px; padding-bottom: 50px;">
          <v-card style="position: fixed; bottom: 40%; right: 9vw; border-radius: 12px;">
            <div class="my-5 mx-3 text-center">
              <v-icon @click="createQuestion(questionForm) + addQuestion()" class="fas fa-plus-circle"></v-icon>
            </div>
            <div>
              <v-row justify="center">
                <v-dialog v-model="dialog" scrollable max-width="600px">
                  <template v-slot:activator="{ on, attrs }">
                    <!-- <v-btn icon class="mx-2 my-2" v-bind="attrs" v-on="on"> -->
                    <div class="mb-5 text-center">
                      <v-icon v-bind="attrs" v-on="on" class="fas fa-palette"></v-icon>
                    </div>
                    <!-- </v-btn> -->
                  </template>
                  <v-card>
                    <v-card-title class="d-flex">
                      <div class="mr-auto">
                        테마 옵션
                      </div>
                      <v-icon @click="closeModal()" class="fas fa-times"></v-icon>
                    </v-card-title>
                    <v-divider></v-divider>
                    <div class="m" style="height: 300px;">
                      <v-btn :title="colors[0]" @click="editSurvey(FormData) + setColor()" fab color="red" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[1]" @click="editSurvey(FormData) + setColor()" fab color="pink" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[2]" @click="editSurvey(FormData) + setColor()" fab color="deep-purple" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[3]" @click="editSurvey(FormData) + setColor()" fab color="indigo" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[4]" @click="editSurvey(FormData) + setColor()" fab color="purple" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[5]" @click="editSurvey(FormData) + setColor()" fab color="blue" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[6]" @click="editSurvey(FormData) + setColor()" fab color="light-blue" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[7]" @click="editSurvey(FormData) + setColor()" fab color="cyan" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[8]" @click="editSurvey(FormData) + setColor()" fab color="teal" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[9]" @click="editSurvey(FormData) + setColor()" fab color="green" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[10]" @click="editSurvey(FormData) + setColor()" fab color="light-green" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[11]" @click="editSurvey(FormData) + setColor()" fab color="lime" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[12]" @click="editSurvey(FormData) + setColor()" fab color="yellow" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[13]" @click="editSurvey(FormData) + setColor()" fab color="amber" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[14]" @click="editSurvey(FormData) + setColor()" fab color="orange" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[15]" @click="editSurvey(FormData) + setColor()" fab color="deep-orange" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[16]" @click="editSurvey(FormData) + setColor()" fab color="brown" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[17]" @click="editSurvey(FormData) + setColor()" fab color="blue-grey" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[18]" @click="editSurvey(FormData) + setColor()" fab color="grey" class="mx-2 mb-2"></v-btn>
                    </div>
                  </v-card>
                </v-dialog>
              </v-row>
            </div>
            <div class="mb-5 text-center">
              <v-icon @click="deleteSurvey(FormData)" class="fas fa-trash-alt"></v-icon>
            </div>
          </v-card>
          <v-card style="margin-left: 20vw; margin-right: 20vw; border-radius: 12px;">
            <div style="margin-left: 2vw; margin-right: 2vw; padding-top: 20px">
              <v-text-field
                v-model="FormData.survey.title"
                @keyup="editSurvey(FormData)"
                label="title"
              ></v-text-field>
            </div>
            <div style="margin-left: 2vw; margin-right: 2vw;">
              <v-text-field
                v-model="FormData.survey.description"
                @keyup="editSurvey(FormData)"
                label="description"
              ></v-text-field>
            </div>
          </v-card>
          <v-card v-for="question in FormData.questions" :key="question.pk" style="margin-left: 20vw; margin-right: 20vw; margin-top: 50px; padding-bottom: 20px; border-radius: 12px;">
            <div class="row" style="margin-left: 1vw; margin-right: 1vw;">
              <div class="col-8 pb-0">
                <v-text-field
                  v-model="question.content"
                  @keyup="editSurvey(FormData)"
                  label="질문"
                ></v-text-field>
              </div>
              <div class="col-4">
                <v-overflow-btn
                  class="my-2"
                  v-model="question.q_type"
                  :items="dropdown_font"
                  label="답변 유형"
                ></v-overflow-btn>
              </div>
            </div>
            <div>
              <div v-for="answer in FormData.answers" :key="answer.pk">
                <div v-if="answer.q_pk === question.pk" class="row" style="margin-left: 1vw;">
                  <v-text-field
                    v-model="answer.content"
                    @keyup="editSurvey(FormData)"
                    label="옵션"
                    solo
                  ></v-text-field>
                  <div class="col-2 py-2">
                    <v-icon :title="answer.pk" @click="deleteOption(answer) + popOption(answer.pk)" class="fas fa-times delete-opbtn"></v-icon>
                  </div>
                </div>
              </div>
              <div v-if="question.q_type === '객관식'" class="py-0" style="margin-left: 1.5vw;">
                <span @click="createOption([answerForm, question.pk]) + addOption(question.pk)" class="text-primary" style="cursor: pointer;">옵션 추가</span>
              </div>
              <div v-else class="col-4 py-0" style="margin-left: 1.1vw;">
                서술형
              </div>
            </div>
            <hr>
            <div class="d-flex justify-content-end">
              <div class="mr-5">
                <v-icon :title="question.pk" @click="deleteQuestion(question) + popQuestion(question.pk)" class="fas fa-trash-alt"></v-icon>
              </div>
            </div>
          </v-card>
        </div>
        <div v-else :style="{ background: FormData.survey.color }" style="height: 100%; padding-top: 50px; padding-bottom: 50px;">
          <v-card style="margin-left: 20vw; margin-right: 20vw; border-radius: 12px; min-width: 500px;">
            <div style="height: 110px; margin-left: 2vw; margin-right: 2vw; padding-top: 20px">
              <strong style="font-size: 30px;">응답 {{ size }}개</strong>
              <v-dialog v-model="nonStudentDialog" scrollable max-width="300px">
                <template v-slot:activator="{ on, attrs }">
                  <span
                    text
                    v-bind="attrs"
                    v-on="on"
                    class="float-right"
                    style="opacity: 0.5;"
                  >
                    설문안한 학생들
                  </span>
                </template>
                <v-card>
                  <v-card-title>설문안한 학생리스트</v-card-title>
                  <v-divider></v-divider>
                  <v-card-text style="height: 300px;">
                    <div v-for="student in Students" :key="student.pk">
                      <div v-if="noResStudentPK.indexOf(student.pk) === -1">
                        {{ student.y_num }}기_{{student.region}}_{{student.class_num}}반_{{student.name}}
                      </div>
                    </div>
                  </v-card-text>
                  <v-divider></v-divider>
                  <v-card-actions>
                    <v-btn color="blue darken-1" text @click="nonStudentDialog = false">취소</v-btn>
                    <v-btn color="blue darken-1" text @click="sendAlert(noResStudentList)">알림 보내기</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </div>
          </v-card>
          <v-card v-for="(response, index) in responses.result" :key="response.pk" style="margin-top: 20px; margin-left: 20vw; margin-right: 20vw; border-radius: 12px; min-width: 500px;">
            <div v-if="response.q_type === '서술형'" style="margin-left: 2vw; margin-right: 2vw; padding-top: 20px">
              <div v-for="question in FormData.questions" :key="question.pk" class="d-flex">
                <h2 v-if="Number(index) === question.pk" class="mb-5 mr-auto">Q.{{ question.content }}</h2>
                <div v-if="Number(index) === question.pk" data-toggle="modal" :href="'#articleCommentList1' + question.pk">          
                  <span style="font-size: 2vh; opacity: 0.5; cursor: pointer;">자세히 보기</span>
                </div>
                <div class="modal" :id="'articleCommentList1' + question.pk" tabindex="-1">
                  <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title">답변 리스트</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body" style="height: 450px; overflow-y: scroll;">
                        <div v-for="answer in answerData" :key="answer.pk">
                          <div v-if="answer.q_pk === question.pk">
                            <div v-for="student in Students" :key="student.pk">
                              <div v-if="student.pk === answer.st_pk">
                                <div class="d-flex mb-2">
                                  <i class="fas fa-user-circle mr-2" style="font-size: 25px; opacity: 0.5;"></i>
                                  <span>{{ student.y_num }}기_{{student.region}}_{{student.class_num}}반_{{student.name}}</span>
                                </div>
                                <p class="mb-5">{{ answer.answer }}</p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div v-for="res in Object.keys(response)" :key="res.pk">
                <v-text-field
                  v-if="res !== 'q_type'"
                  :value="res"
                  label="Solo"
                  solo
                  disabled
                ></v-text-field>
              </div>
            </div>
            <div v-else-if="response.q_type === '객관식'" style="margin-left: 2vw; margin-right: 2vw; padding-top: 20px; padding-bottom: 20px;">
              <div v-for="question in FormData.questions" :key="question.pk">
                <div v-if="Number(index) === question.pk">
                  <div class="d-flex">
                    <h5 class="mb-5 mr-auto">Q.{{ question.content }}</h5>
                    <div data-toggle="modal" :href="'#articleCommentList2' + question.pk">          
                      <span class="mr-3" style="font-size: 2vh; opacity: 0.5; cursor: pointer;">자세히 보기</span>
                    </div>
                    <div class="modal" :id="'articleCommentList2' + question.pk" tabindex="-1">
                      <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                          <div class="modal-header">
                            <h5 class="modal-title">답변 리스트</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                            </button>
                          </div>
                          <div class="modal-body">
                            <div v-for="a in FormData.answers" :key="a.pk">
                              <div v-if="a.q_pk === question.pk">
                                <h1>{{ a.content }}</h1>
                                <div v-if="Object.keys(response).indexOf(String(a.pk)) === -1">
                                  없음
                                </div>
                                <div v-else>
                                  <div v-for="answer in answerData" :key="answer.pk">
                                    <div v-if="a.pk === Number(answer.answer)">
                                      <div v-for="student in Students" :key="student.pk">
                                        <div v-if="student.pk === answer.st_pk" class="d-flex">
                                          <div class="mr-5 mb-2">
                                            <i class="fas fa-user-circle mr-2" style="font-size: 25px; opacity: 0.5;"></i>
                                            <span>{{ student.y_num }}기_{{student.region}}_{{student.class_num}}반_{{student.name}}</span>
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style="margin-left: 10vw">
                    <VueChart :questionData="question" :answerData="FormData.answers" :responseData="response"></VueChart>
                  </div>
                </div>
              </div>
            </div>
          </v-card>
        </div>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import Nav from '@/components/Nav.vue'
import VueChart from '@/components/VueChart.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    Nav,
    VueChart,
  },
  created() {
    this.getStudents()
    if(Object.values(this.responses.result)[0]) {
      Object.values(Object.values(this.responses.result)[0]).forEach(element => {
        if(Number.isInteger(element)) {
          this.size += element
        }
      });
    }
    this.originColor = this.originFormData.survey.color
    // console.log(this.responses)
    // console.log(this.Students)
    // console.log(this.answerData)
    this.answerData.forEach(answer => {
      if(!this.noResStudentPK || this.noResStudentPK.indexOf(answer.st_pk) === -1) {
        this.noResStudentPK.push(answer.st_pk)
      }
    })
    this.Students.forEach(student => {
      if(this.noResStudentPK.indexOf(student.pk) === -1) {
        this.noResStudentList.push(`${student.region}_${student.class_num}반_${student.name}`)
      }
    });
    console.log(this.noResStudentList)
  },
  mounted() {
    this.FormData = this.originFormData
    this.FormData.survey.color = this.originFormData.survey.color
    this.questionForm.surveyss.push(this.originFormData.survey.pk)
    this.answerForm.s_pk = this.originFormData.survey.pk
  },
  data() {
    return {
      isZero: true,
      nonStudentDialog: false,
      size: 0,
      colors: [
               'red', 'pink', 'deep-purple', 
               'indigo', 'purple', 'blue', 
               'light-blue', 'cyan', 'teal', 
               'green', 'light-green', 'lime',
               'yellow', 'amber', 'orange',
               'deep-orange', 'brown', 'blue-grey',
               'grey', 
      ],
      originColor: null,
      activeColor: '#FFCDD2',
      dialogm1: '',
      dialog: false,
      sList_mult: false,
      sList_essay: false,
      tab: null,
      items: ['설문', '응답'],
      FormData: {
        answers: [],
        questions: [], 
        survey: {
          pk: null,
          title: 'title',
          description: 'description',
          color: null,
          user: {
            pk: null,
            username: null,
            email: null
          }
        },
      },
      dropdown_font: ['객관식', '서술형'],
      questionForm: {
        pk: null,
        q_type: '객관식',
        content: null,
        surveyss: [],
      },
      answerForm: {
        pk: null,
        s_pk: null,
        q_pk: null,
        content: null,
      },
      results: [],
      noResStudentPK: [],
      noResStudentList: [],
    }
  },
  methods: {
    ...mapActions(['saveSurvey', 'sendAlert', 'editSurvey', 'deleteSurvey', 'createQuestion', 'createOption', 'deleteQuestion', 'deleteOption', 'fetchStudentResponse', 'getStudents']),
    addQuestion() {
      this.FormData.questions.push({
        pk: null,
        q_type: '객관식',
        content: null,
        surveyss: [this.FormData.survey.pk]
      })
    },
    addOption(pk) {
      this.FormData.answers.push({
        pk: null,
        s_pk: this.FormData.survey.pk,
        q_pk: pk,
        content: null,
      })
    },
    popQuestion(pk) {
      const findItem = this.FormData.questions.find(function (item) {
        return item.pk === pk;
      });
      const idx = this.FormData.questions.indexOf(findItem);
      this.FormData.questions.splice(idx, 1);
    },
    popOption(pk) {
      const findItem = this.FormData.answers.find(function (item) {
        return item.pk === pk;
      });
      const idx = this.FormData.answers.indexOf(findItem);
      this.FormData.answers.splice(idx, 1);
    },
    setColor() {
      const color = event.target.title
      if (color === 'red') {
        this.activeColor = '#FFCDD2'
        this.FormData.survey.color = '#FFCDD2'
      } else if (color === 'purple') {
        this.activeColor = '#F3E5F5'
        this.FormData.survey.color = '#F3E5F5'
      } else if (color === 'blue') {
        this.activeColor = '#BBDEFB'
        this.FormData.survey.color = '#BBDEFB'
      } else if (color === 'pink') {
        this.activeColor = '#F8BBD0'
        this.FormData.survey.color = '#F8BBD0'
      } else if (color === 'deep-purple') {
        this.activeColor = '#D1C4E9'
        this.FormData.survey.color = '#D1C4E9'
      } else if (color === 'indigo') {
        this.activeColor = '#C5CAE9'
        this.FormData.survey.color = '#C5CAE9'
      } else if (color === 'light-blue') {
        this.activeColor = '#B3E5FC'
        this.FormData.survey.color = '#B3E5FC'
      } else if (color === 'cyan') {
        this.activeColor = '#B2EBF2'
        this.FormData.survey.color = '#B2EBF2'
      } else if (color === 'teal') {
        this.activeColor = '#B2DFDB'
        this.FormData.survey.color = '#B2DFDB'
      } else if (color === 'green') {
        this.activeColor = '#C8E6C9'
        this.FormData.survey.color = '#C8E6C9'
      } else if (color === 'light-green') {
        this.activeColor = '#DCEDC8'
        this.FormData.survey.color = '#DCEDC8'
      } else if (color === 'lime') {
        this.activeColor = '#F0F4C3'
        this.FormData.survey.color = '#F0F4C3'
      } else if (color === 'yellow') {
        this.activeColor = '#FFF9C4'
        this.FormData.survey.color = '#FFF9C4'
      } else if (color === 'amber') {
        this.activeColor = '#FFECB3'
        this.FormData.survey.color = '#FFECB3'
      } else if (color === 'orange') {
        this.activeColor = '#FFE0B2'
        this.FormData.survey.color = '#FFE0B2'
      } else if (color === 'deep-orange') {
        this.activeColor = '#FFCCBC'
        this.FormData.survey.color = '#FFCCBC'
      } else if (color === 'brown') {
        this.activeColor = '#D7CCC8'
        this.FormData.survey.color = '#D7CCC8'
      } else if (color === 'blue-grey') {
        this.activeColor = '#CFD8DC'
        this.FormData.survey.color = '#CFD8DC'
      } else if (color === 'grey') {
        this.activeColor = '#F5F5F5'
        this.FormData.survey.color = '#F5F5F5'
      }
    },
    closeModal() {
      this.dialog = false
    },
  },
  computed: {
    ...mapState(['originFormData', 'isSaved', 'responses', 'Students', 'answerData'])
  },
}
</script>

<style>
.container {
  margin-top: 50px;
  margin-bottom: 50px;
}

.modal-body::-webkit-scrollbar {
    display: none;
}
</style>
