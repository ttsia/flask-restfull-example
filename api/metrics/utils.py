# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: utils
# Created: 2019-05-08
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
Metrics module helper for pylint report generation
"""
import os
from flask import current_app
from pylint import epylint
from werkzeug.exceptions import abort


def get_files_to_check():
    """
    :return: files to be checked string
    """
    files = current_app.config.get('PYLINT_SETTINGS').get('include')
    if not files:
        abort(400, 'MISSING PYLINT_SETTINGS.include value')
    try:
        return ' '.join(files)
    except TypeError:
        abort(400, 'PYLINT_SETTINGS.INCLUDE items should be strings')
    except Exception as exception:
        abort(400, str(exception))


def create_report_dir():
    """
    :return: report directory path
    """
    directory = current_app.config.get('PYLINT_SETTINGS').get('report_directory_name')
    if not directory:
        abort(400, 'MISSING PYLINT_SETTINGS.report_directory_name value')
    path = os.path.join(current_app.static_folder, directory)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_report_file(dir_path):
    """
    :param dir_path:
    :return: report file path
    """
    filename = current_app.config.get('PYLINT_SETTINGS').get('report_file_name')
    if not filename:
        abort(400, 'MISSING PYLINT_SETTINGS.report_file_name value')
    path = os.path.join(current_app.static_folder, dir_path, filename)
    return path


def get_config_opts():
    """
    :return: path to pylint configuration file
    """
    path = os.path.join(current_app.config.get('PYLINT_SETTINGS').get('config_directory_name', ""), current_app.config.get('PYLINT_SETTINGS').get('config_file_name', ""))
    if not os.path.exists(path):
        return ""
    return "  --rcfile={0}".format(path)


def generate_report():
    """
    Get pylint analization report and write it to file
    """
    files = get_files_to_check()
    dir_path = create_report_dir()
    file_path = create_report_file(dir_path)
    config_opts = get_config_opts()
    pylint_opts = '--load-plugins pylint_flask' + config_opts
    pylint_stdout, pylint_stderr = epylint.py_run(files + ' ' + pylint_opts, return_std=True)
    with open(file_path, 'w+') as report:
        report.write(pylint_stdout.getvalue())
        report.write(pylint_stderr.getvalue())
    return True
