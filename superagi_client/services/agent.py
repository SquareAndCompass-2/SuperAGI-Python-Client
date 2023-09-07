from typing import Optional, List

from pydantic import validate_arguments

from superagi_client.dto.agent_config import AgentConfig
from superagi_client.dto.agent_update_config import AgentUpdateConfig
from superagi_client.dto.agent_execution import AgentExecution
from superagi_client.dto.agent_run_filter import AgentRunFilter
from superagi_client.lib.superagi import Superagi


class Agent:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        superagi=None,
    ):
        self.base_url = base_url
        self.api_key = api_key

        if superagi is None:
            superagi = Superagi(base_url=self.base_url, api_key=self.api_key)
        self.superagi = superagi

    @validate_arguments
    def create(self, agent_config: AgentConfig):
        response = self.superagi.create_agent(agent_config=agent_config)
        return response

    @validate_arguments
    def update(self, agent_id: int, agent_update_config: AgentUpdateConfig):
        response = self.superagi.update_agent(
            agent_id=agent_id, agent_update_config=agent_update_config
        )
        return response

    @validate_arguments
    def pause(self, agent_id: int, agent_execution_ids: Optional[List[int]] = None):
        response = self.superagi.pause_agent(
            agent_id=agent_id, agent_execution_ids=agent_execution_ids
        )
        return response

    @validate_arguments
    def resume(self, agent_id: int, agent_execution_ids: Optional[List[int]] = None):
        response = self.superagi.resume_agent(
            agent_id=agent_id, agent_execution_ids=agent_execution_ids
        )
        return response

    @validate_arguments
    def create_run(
        self, agent_id: int, agent_execution: Optional[AgentExecution] = None
    ):
        response = self.superagi.create_agent_run(
            agent_id=agent_id, agent_execution=agent_execution
        )
        return response

    @validate_arguments
    def get_run_status(
        self, agent_id: int, agent_run_filter: Optional[AgentRunFilter] = None
    ):
        response = self.superagi.get_agent_run_status(
            agent_id=agent_id, agent_run_filter=agent_run_filter
        )
        return response

    @validate_arguments
    def get_run_resources(self, agent_resource_ids: List[int]):
        response = self.superagi.get_agent_run_resources(
            agent_resource_ids=agent_resource_ids
        )
        return response