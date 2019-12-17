<template>
      <v-flex
        xs12
        mt-5
      >
        <h2 v-if="chartData.length > 0" class="headline font-weight-bold mb-3">Word Cloud</h2>
        <highcharts v-if="chartData.length > 0" :options="chartOptions"></highcharts>
      </v-flex>
</template>

<script>
    export default {
        name: 'SelectCIKs',
        props: ['chartData'],
        data: () => ({
            chartOptions: {
              // accessibility: {
              //     screenReaderSection: {
              //         beforeChartFormat: '<h5>{chartTitle}</h5>' +
              //             '<div>{chartSubtitle}</div>' +
              //             '<div>{chartLongdesc}</div>' +
              //             '<div>{viewTableButton}</div>'
              //     }
              // },
              series: [{
                  type: 'wordcloud',
                  data:  [{
                        name: 'sample1',
                        weight: 3
                    }, {
                        name: 'sample2',
                        weight: 2
                    }, {
                        name: 'sample3',
                        weight: 1
                  }],
                  name: 'Weight'
              }],
              title: {
                  text: 'LDA generated words'
              }
            }
        }),
        mounted () {
        },
        watch: {
            chartData: function () {

            }
        }
    };
</script>
