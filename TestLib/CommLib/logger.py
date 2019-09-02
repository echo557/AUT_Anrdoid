# coding: utf-8
import logging
import logging.config

class logger():
     # def __init__(self, logname, loglevel, logger):
    def __init__(self):
    #     '''
    #        指定保存日志的文件路径，日志级别，以及调用文件
    #        将日志存入到指定的文件中
    #     '''
    #
    #     # 创建一个logger
         self.logger = logging.getLogger()
    #     self.logger.setLevel(logging.DEBUG)
    #
    #     # 创建一个handler，用于写入日志文件
    #     fh = logging.FileHandler(logname)
    #     fh.setLevel(logging.DEBUG)
    #
    #     # 再创建一个handler，用于输出到控制台
    #     ch = logging.StreamHandler()
    #     ch.setLevel(logging.DEBUG)
    #
    #     # 定义handler的输出格式
    #     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #     # formatter = format_dict[int(loglevel)]
    #     fh.setFormatter(formatter)
    #     ch.setFormatter(formatter)
    #
    #     # 给logger添加handler
    #     self.logger.addHandler(fh)
    #     self.logger.addHandler(ch)


    def getlog(self):
        return self.logger

    def showError(self, xiaoxi):

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # formatter = format_dict[int(loglevel)]
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(ch)
        self.logger.info(xiaoxi)




# class logger():
#
#
#     def __init__(self):
#         conf = {'version': 1,
#                 'disable_existing_loggers': True,
#                 'incremental': False,
#                 'formatters': {'myformat_INFO': {'class': 'logging.Formatter',
#                                                  'format': '%(message)s',
#                                                  'datefmt': '%Y-%m-%d %H:%M:%S'},
#                                'myformat_ERROR': {'class': 'logging.Formatter',
#                                                   'format': '|%(asctime)s|%(filename)s|%(lineno)d|%(funcName)s|%(levelname)s|%(message)s',
#                                                   'datefmt': '%Y-%m-%d %H:%M:%S'}
#                                },
#                 # 'filters': {'filter_by_name': {'class': 'logging.Filter',
#                 #                                'name': 'logger_for_filter_name'},
#                 #
#                 #             'filter_single_level_pass': {'()': 'mylogger.SingleLevelFilter',
#                 #                                          'pass_level': logging.WARN}
#                 #             },
#                 'handlers': {'console_INFO': {'class': 'logging.StreamHandler',
#                                               # 'level': 'DEBUG',
#                                               'formatter': 'myformat_INFO',
#                                               # 'filters': ['filter_single_level_pass', ]
#                                               },
#                              'console_ERROR': {'class': 'logging.StreamHandler',
#                                                # 'level': 'DEBUG',
#                                                'formatter': 'myformat_ERROR',
#                                                # 'filters': ['filter_single_level_pass', ]
#                                                },
#                              #  'screen': {'()': 'mylogger.ScreenHandler',
#                              #             'level': logging.INFO,
#                              # #            'formatter': 'myformat1',
#                              # #            # 'filters': ['filter_by_name', ]
#                              #             }
#                              },
#                 'loggers': {'logger_for_ERROR': {'handlers': ['console_ERROR'],
#                                                        # 'filters': ['filter_by_name', ],
#                                                        'level': 'DEBUG'},
#                             'logger_for_INFO': {'handlers': ['console_INFO', ],
#                                                # 'filters': ['filter_single_level_pass', ],
#                                                'level': 'DEBUG',
#                                                'propagate': False}
#                             }
#                 }
#         logging.config.dictConfig(conf)
#
#
# if __name__ == '__main__':
#     init_logger()
#     logger_for_filter_name = logging.getLogger('logger_for_filter_name')
#     logger_for_filter_name.debug('logger_for_filter_name')
#     logger_for_filter_name.info('logger_for_filter_name')
#     # logger_for_filter_name.warn('logger_for_filter_name')
#     logger_for_filter_name.error('logger_for_filter_name')
#     logger_for_filter_name.critical('logger_for_filter_name')
#
#     logger_for_all = logging.getLogger('logger_for_all')
#     logger_for_all.debug('logger_for_all')
#     logger_for_all.info('logger_for_all')
#     # logger_for_all.warn('logger_for_all')
#     logger_for_all.error('logger_for_all')
#     logger_for_all.critical('HEHHEHE')
