package com.petflix.films

import org.slf4j.LoggerFactory
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.info.GitProperties
import org.springframework.scheduling.annotation.EnableScheduling

@SpringBootApplication
@EnableScheduling
open class FilmStreamingServicesApp {

   companion object {
      val logger = LoggerFactory.getLogger(this::class.java)

      @JvmStatic
      fun main(args: Array<String>) {
         SpringApplication.run(FilmStreamingServicesApp::class.java, *args)
      }
   }

   @Autowired
   fun logInfo(@Autowired(required = false) buildInfo: GitProperties? = null) {
      val commit = buildInfo?.shortCommitId ?: "Unknown"
      logger.info("Films API built on commit $commit")
   }
}
