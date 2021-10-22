<!-- markdownlint-disable -->

# API Overview

## Modules

- [`ansible`](./ansible.md#module-ansible): Main Ansible Module Builder.
- [`cli`](./cli.md#module-cli): common cli attributes.
- [`cli.subcommands`](./cli.subcommands.md#module-clisubcommands): cli subcommands.
- [`cli.templates`](./cli.templates.md#module-clitemplates): Templates for creating new modules.
- [`environment`](./environment.md#module-environment): Environment variables, configuration and static filepaths.
- [`exceptions`](./exceptions.md#module-exceptions): Exceptions for application.
- [`hooks`](./hooks.md#module-hooks): base classes for hooks module.
- [`hooks.config`](./hooks.config.md#module-hooksconfig): constants for module.
- [`hooks.dest_types`](./hooks.dest_types.md#module-hooksdest_types)
- [`hooks.dest_types.executable`](./hooks.dest_types.executable.md#module-hooksdest_typesexecutable): Executable type.
- [`hooks.dest_types.slack_webhook`](./hooks.dest_types.slack_webhook.md#module-hooksdest_typesslack_webhook): Abstract method for other modules.
- [`hooks.dest_types.webhook_no_auth`](./hooks.dest_types.webhook_no_auth.md#module-hooksdest_typeswebhook_no_auth): Executable type.
- [`hooks.registry`](./hooks.registry.md#module-hooksregistry): response hook registry
- [`host`](./host.md#module-host)
- [`host.intro`](./host.intro.md#module-hostintro): Introduction builder.
- [`host.main_intro_data`](./host.main_intro_data.md#module-hostmain_intro_data): Question data interfaces.
- [`host.mods`](./host.mods.md#module-hostmods): Abstract method for other modules.
- [`host.nav`](./host.nav.md#module-hostnav): Navigation related utils.
- [`host.question_data`](./host.question_data.md#module-hostquestion_data): Question data interfaces.
- [`host.question_state`](./host.question_state.md#module-hostquestion_state): Abstract method for other modules.
- [`host.registry`](./host.registry.md#module-hostregistry): Question data interfaces.
- [`host.userdata`](./host.userdata.md#module-hostuserdata): Userdata / bootstrap module.
- [`host.xonsh`](./host.xonsh.md#module-hostxonsh): XenSH question interface.

## Classes

- [`ansible.Ansible`](./ansible.md#class-ansible): Ansible.
- [`cli.MainParser`](./cli.md#class-mainparser): MainParser.
- [`cli.ParserWrap`](./cli.md#class-parserwrap): ParserWrap.
- [`subcommands.AssembleQuestions`](./cli.subcommands.md#class-assemblequestions): AssembleQuestions.
- [`subcommands.Bootstrap`](./cli.subcommands.md#class-bootstrap): Bootstrap.
- [`subcommands.CreateNewModule`](./cli.subcommands.md#class-createnewmodule): CreateNewModule.
- [`subcommands.Demo`](./cli.subcommands.md#class-demo): Demo.
- [`subcommands.RunAllModules`](./cli.subcommands.md#class-runallmodules): RunAllModules.
- [`subcommands.RunModule`](./cli.subcommands.md#class-runmodule): RunModule.
- [`subcommands.SaveUserData`](./cli.subcommands.md#class-saveuserdata): SaveUserData.
- [`subcommands.TestQuestions`](./cli.subcommands.md#class-testquestions): TestQuestions.
- [`environment.InterviewConfig`](./environment.md#class-interviewconfig): InterviewConfig.
- [`exceptions.ErrorBadConfig`](./exceptions.md#class-errorbadconfig): Throw if the main configuration is bad.
- [`exceptions.PreCheckFail`](./exceptions.md#class-precheckfail): Throw if Terraform precheck fails.
- [`hooks.Hook`](./hooks.md#class-hook): BaseHookType.
- [`executable.ExecutableDest`](./hooks.dest_types.executable.md#class-executabledest): ExecutableDest.
- [`slack_webhook.SlackSend`](./hooks.dest_types.slack_webhook.md#class-slacksend): Send slack messages to ops-interviews channel.
- [`slack_webhook.SlackWebhook`](./hooks.dest_types.slack_webhook.md#class-slackwebhook): WebHookNoAuth.
- [`webhook_no_auth.WebHookNoAuth`](./hooks.dest_types.webhook_no_auth.md#class-webhooknoauth): WebHookNoAuth.
- [`registry.HookLoader`](./hooks.registry.md#class-hookloader): Loader.
- [`intro.Intro`](./host.intro.md#class-intro): Intro.
- [`main_intro_data.MainIntroCollection`](./host.main_intro_data.md#class-mainintrocollection): MainIntroCollection.
- [`main_intro_data.MainIntroData`](./host.main_intro_data.md#class-mainintrodata): MainIntroData.
- [`mods.BaseModule`](./host.mods.md#class-basemodule): Module interface.
- [`mods.MainIntroModule`](./host.mods.md#class-mainintromodule)
- [`mods.ModuleLoader`](./host.mods.md#class-moduleloader)
- [`mods.ModulesCollection`](./host.mods.md#class-modulescollection): Collection of modules.
- [`mods.QuestionModule`](./host.mods.md#class-questionmodule)
- [`mods.SystemModule`](./host.mods.md#class-systemmodule)
- [`nav.NavFooter`](./host.nav.md#class-navfooter): NavFooter.
- [`nav.Navigation`](./host.nav.md#class-navigation): Navigation.
- [`question_data.QuestionCollection`](./host.question_data.md#class-questioncollection): ModuleQuestions.
- [`question_data.QuestionData`](./host.question_data.md#class-questiondata): QuestionModule.
- [`question_state.StateData`](./host.question_state.md#class-statedata): StateData.
- [`registry.DataInterface`](./host.registry.md#class-datainterface): Required Data interface for Registry.
- [`registry.RegistryBase`](./host.registry.md#class-registrybase): ModuleQuestions.
- [`userdata.UserDataScript`](./host.userdata.md#class-userdatascript): UserDataScript.
- [`xonsh.QuestionPrompt`](./host.xonsh.md#class-questionprompt): QuestionPrompt.

## Functions

- [`subcommands.yesno`](./cli.subcommands.md#function-yesno): Simple Yes/No Function.
- [`templates.copy_type`](./cli.templates.md#function-copy_type): copy_type.
- [`intro.intro_export_b64`](./host.intro.md#function-intro_export_b64): intro_export_b64.
- [`intro.intro_load_pickle_b64`](./host.intro.md#function-intro_load_pickle_b64): intro_load_pickle_b64.
- [`intro.show_all_colors`](./host.intro.md#function-show_all_colors): show_all_colors.
- [`nav.color`](./host.nav.md#function-color): color.
- [`userdata.main`](./host.userdata.md#function-main): Run main function.
- [`xonsh.bash_filter`](./host.xonsh.md#function-bash_filter): bash_filter.
- [`xonsh.cmd_event`](./host.xonsh.md#function-cmd_event): cmd_event.
- [`xonsh.height`](./host.xonsh.md#function-height): height.
- [`xonsh.twrap`](./host.xonsh.md#function-twrap): twrap.
- [`xonsh.width`](./host.xonsh.md#function-width): width.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
