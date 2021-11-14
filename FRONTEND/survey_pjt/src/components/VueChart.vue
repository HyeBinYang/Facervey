<template>
  <div>
    <apexchart width="400" type="pie" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  components: {
    apexchart: VueApexCharts,
  },
  props: ["questionData", "responseData", "answerData"],
  data() {
    return {
      q_pk: null,
      series: [],
      chartOptions: {
          chart: {
              width: 380,
              type: 'pie',
          },
          labels: [],
          responsive: [{
              breakpoint: 480,
              options: {
                  chart: {
                      width: 200
                  },
                  legend: {
                      position: 'bottom'
                  }
              }
          }]
      },
    }
  },
  created() {
    this.q_pk = this.questionData.pk
    this.answerData.forEach(answer => {
      if(answer.q_pk === this.q_pk) {
        this.chartOptions.labels.push(answer.content)
        if(Object.keys(this.responseData).indexOf(String(answer.pk)) !== -1) {
          this.series.push(Object.values(this.responseData)[Object.keys(this.responseData).indexOf(String(answer.pk))])
        }
        else {
          this.series.push(0)
        }
      }
    });
  },
}
</script>

<style>
</style>