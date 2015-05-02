"""
 * Initial import of zookeepr tables

Revision ID: 2daf319bbf1
Revises: None
Create Date: 2012-06-10 11:22:51.540533

"""

# revision identifiers, used by Alembic.
revision = '2daf319bbf1'
down_revision = None

from alembic import op
import sqlalchemy as sa
from zk import model
from zk.model import meta


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_hash',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.Text(), nullable=False),
    sa.Column('url_hash', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url'),
    sa.UniqueConstraint('url_hash')
    )
    op.create_table('travel_assistance_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('accommodation_assistance_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('proposal_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('target_audience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rego_id', sa.Integer(), nullable=True),
    sa.Column('vote_value', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_content_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('funding_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('note', sa.String(), nullable=True),
    ##sa.CheckConstraint('TODO'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('password_reset_confirmation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_address', sa.Text(), nullable=False),
    sa.Column('url_hash', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address'),
    sa.UniqueConstraint('url_hash')
    )
    op.create_table('stream',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('funding_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('special_offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('id_name', sa.Text(), nullable=True),
    #sa.CheckConstraint('TODO'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('proposal_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ceiling',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('max_sold', sa.Integer(), nullable=True),
    sa.Column('available_from', sa.DateTime(), nullable=True),
    sa.Column('available_until', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.Text(), nullable=False),
    sa.Column('display_order', sa.Integer(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_address', sa.Text(), nullable=False),
    sa.Column('password_hash', sa.Text(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.Column('url_hash', sa.String(length=32), nullable=False, index=True),
    sa.Column('activated', sa.Boolean(), nullable=False),
    sa.Column('firstname', sa.Text(), nullable=True),
    sa.Column('lastname', sa.Text(), nullable=True),
    sa.Column('address1', sa.Text(), nullable=True),
    sa.Column('address2', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('postcode', sa.Text(), nullable=True),
    sa.Column('country', sa.Text(), nullable=True),
    sa.Column('company', sa.Text(), nullable=True),
    sa.Column('phone', sa.Text(), nullable=True),
    sa.Column('mobile', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('experience', sa.Text(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('badge_printed', sa.Boolean(), nullable=True),
    sa.Column('i_agree', sa.types.Boolean, nullable=False, default=False),
    #sa.CheckConstraint('TODO'),
    #sa.CheckConstraint('TODO'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address')
    )
    op.create_table('social_network',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('url', sa.Text(), nullable=False),
    sa.Column('logo', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('display_order', sa.Integer(), nullable=False),
    sa.Column('display', sa.Text(), nullable=False),
    sa.Column('display_mode', sa.Text(), nullable=True),
    sa.Column('invoice_free_products', sa.Boolean(), nullable=False),
    sa.Column('min_qty', sa.Integer(), nullable=True),
    sa.Column('max_qty', sa.Integer(), nullable=True),
    #sa.CheckConstraint('TODO'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('pretty_name', sa.Text(), nullable=True),
    sa.Column('display_order', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('time_slot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('primary', sa.Boolean(), nullable=False),
    sa.Column('heading', sa.Boolean(), nullable=False),
    sa.CheckConstraint('(start_time < end_time)', name='time_slot_check'),
    #sa.CheckConstraint('TODO'),
    #sa.CheckConstraint('TODO'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('start_time','end_time')
    )
    op.create_table('person_role_map',
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], onupdate='CASCADE', ondelete='CASCADE' ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'] ,onupdate='CASCADE', ondelete='CASCADE' ),
    sa.PrimaryKeyConstraint('person_id', 'role_id')
    )
    op.create_table('proposal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('abstract', sa.Text(), nullable=True),
    sa.Column('technical_requirements', sa.Text(), nullable=True),
    sa.Column('proposal_type_id', sa.Integer(), nullable=False),
    sa.Column('stream_id', sa.Integer(), nullable=True),
    sa.Column('travel_assistance_type_id', sa.Integer(), nullable=False),
    sa.Column('accommodation_assistance_type_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('target_audience_id', sa.Integer(), nullable=False),
    sa.Column('video_release', sa.Boolean(), nullable=True),
    sa.Column('slides_release', sa.Boolean(), nullable=True),
    sa.Column('project', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('abstract_video_url', sa.Text(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    ##sa.CheckConstraint('TODO'),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['accommodation_assistance_type_id'], ['accommodation_assistance_type.id'], ),
    sa.ForeignKeyConstraint(['proposal_type_id'], ['proposal_type.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['proposal_status.id'], ),
    sa.ForeignKeyConstraint(['stream_id'], ['stream.id'], ),
    sa.ForeignKeyConstraint(['target_audience_id'], ['target_audience.id'], ),
    sa.ForeignKeyConstraint(['travel_assistance_type_id'], ['travel_assistance_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('special_registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_number', sa.Text(), nullable=True),
    sa.Column('special_offer_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['special_offer_id'], ['special_offer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('manual', sa.Boolean(), nullable=False),
    sa.Column('void', sa.String(), nullable=True),
    sa.Column('issue_date', sa.DateTime(), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funding',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('funding_type_id', sa.Integer(), nullable=True),
    sa.Column('male', sa.Boolean(), nullable=True),
    sa.Column('why_attend', sa.Text(), nullable=True),
    sa.Column('how_contribute', sa.Text(), nullable=True),
    sa.Column('financial_circumstances', sa.Text(), nullable=True),
    sa.Column('diverse_groups', sa.Text(), nullable=True),
    sa.Column('supporting_information', sa.Text(), nullable=True),
    sa.Column('prevlca', sa.String(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['funding_type_id'], ['funding_type.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['funding_status.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('person_id','funding_type_id')
    )
    op.create_table('voucher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Text(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('leader_id', sa.Integer(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['leader_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('person_social_network_map',
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('social_network_id', sa.Integer(), nullable=False),
    sa.Column('account_name', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], onupdate='CASCADE', ondelete='CASCADE' ),
    sa.ForeignKeyConstraint(['social_network_id'], ['social_network.id'], onupdate='CASCADE', ondelete='CASCADE' ),
    sa.PrimaryKeyConstraint('person_id', 'social_network_id'),
    sa.UniqueConstraint('person_id','social_network_id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('auth', sa.Text(), nullable=True),
    sa.Column('validate', sa.Text(), nullable=True),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['category_id'], ['product_category.id'], onupdate='CASCADE', ondelete='CASCADE' ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category_id','description')
    )
    op.create_table('db_content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('publish_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['type_id'], ['db_content_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=False),
    sa.Column('reviewer_id', sa.Integer(), nullable=False),
    sa.Column('stream_id', sa.Integer(), nullable=True),
    sa.Column('miniconf', sa.Text(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('private_comment', sa.Text(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], ),
    sa.ForeignKeyConstraint(['reviewer_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['stream_id'], ['stream.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('proposal_id','reviewer_id', name='ux_review_proposal_reviewer')
    )
    op.create_table('person_proposal_map',
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], onupdate='CASCADE', ondelete='CASCADE' ),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], onupdate='CASCADE', ondelete='CASCADE' ),
    sa.PrimaryKeyConstraint('person_id', 'proposal_id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=False),
    sa.Column('exclusive', sa.Boolean(), nullable=False),
    sa.Column('sequence', sa.Integer(), nullable=False),
    #sa.CheckConstraint('TODO'),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['event_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('proposal_id')
    )
    op.create_table('volunteer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('areas', sa.String(), nullable=False),
    sa.Column('other', sa.Text(), nullable=False),
    sa.Column('experience', sa.Text(), nullable=True),
    sa.Column('accepted', sa.Boolean(), nullable=True),
    sa.Column('ticket_type_id', sa.Integer(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['ticket_type_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('person_id')
    )
    op.create_table('product_include',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('include_category_id', sa.Integer(), nullable=False),
    sa.Column('include_qty', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['include_category_id'], ['product_category.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'include_category_id')
    )
    op.create_table('registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('over18', sa.Boolean(), nullable=True),
    sa.Column('nick', sa.Text(), nullable=True),
    sa.Column('shell', sa.Text(), nullable=True),
    sa.Column('editor', sa.Text(), nullable=True),
    sa.Column('distro', sa.Text(), nullable=True),
    sa.Column('vcs', sa.Text(), nullable=True),
    sa.Column('silly_description', sa.Text(), nullable=True),
    sa.Column('keyid', sa.Text(), nullable=True),
    sa.Column('planetfeed', sa.Text(), nullable=True),
    sa.Column('voucher_code', sa.Text(), nullable=True),
    sa.Column('diet', sa.Text(), nullable=True),
    sa.Column('special', sa.Text(), nullable=True),
    sa.Column('partner_name', sa.Text(), nullable=True),
    sa.Column('partner_email', sa.Text(), nullable=True),
    sa.Column('partner_mobile', sa.Text(), nullable=True),
    sa.Column('prevlca', sa.String(), nullable=True),
    sa.Column('signup', sa.String(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['voucher_code'], ['voucher.code'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('person_id'),
    sa.UniqueConstraint('voucher_code')
    )
    op.create_table('attachment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.Text(), nullable=False),
    sa.Column('content_type', sa.Text(), nullable=False),
    sa.Column('content', sa.LargeBinary(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_creation_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('free_qty', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funding_attachment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('funding_id', sa.Integer(), nullable=True),
    sa.Column('filename', sa.Text(), nullable=False),
    sa.Column('content_type', sa.Text(), nullable=False),
    sa.Column('content', sa.LargeBinary(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_creation_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['funding_id'], ['funding.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_ceiling_map',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('ceiling_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ceiling_id'], ['ceiling.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'ceiling_id')
    )
    op.create_table('funding_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('funding_id', sa.Integer(), nullable=False),
    sa.Column('reviewer_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['funding_id'], ['funding.id'], ),
    sa.ForeignKeyConstraint(['reviewer_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('funding_id','reviewer_id')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voucher_product',
    sa.Column('voucher_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('percentage', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['voucher_id'], ['voucher.id'], ),
    sa.PrimaryKeyConstraint('voucher_id', 'product_id')
    )
    op.create_table('registration_product_map',
    sa.Column('registration_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['registration_id'], ['registration.id'], ),
    sa.PrimaryKeyConstraint('registration_id', 'product_id')
    )
    op.create_table('payment_received',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=False),
    sa.Column('validation_errors', sa.String(), nullable=True),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.Column('success_code', sa.String(), nullable=False),
    sa.Column('amount_paid', sa.Integer(), nullable=True),
    sa.Column('currency_used', sa.String(), nullable=True),
    sa.Column('auth_code', sa.String(), nullable=True),
    sa.Column('card_name', sa.String(), nullable=True),
    sa.Column('card_type', sa.String(), nullable=True),
    sa.Column('card_number', sa.String(), nullable=True),
    sa.Column('card_expiry', sa.String(), nullable=True),
    sa.Column('card_mac', sa.String(), nullable=True),
    sa.Column('gateway_ref', sa.String(), nullable=True),
    sa.Column('response_text', sa.String(), nullable=False),
    sa.Column('client_ip_zk', sa.String(), nullable=False),
    sa.Column('client_ip_gateway', sa.String(), nullable=False),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], ),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_slot_id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('overflow', sa.Boolean(), nullable=True),
    sa.Column('video_url', sa.Text(), nullable=True),
    sa.Column('audio_url', sa.Text(), nullable=True),
    sa.Column('slide_url', sa.Text(), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    #sa.CheckConstraint('TODO'),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['time_slot_id'], ['time_slot.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('time_slot_id','location_id')
    )
    op.create_table('rego_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rego_id', sa.Integer(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('by_id', sa.Integer(), nullable=False),
    sa.Column('creation_timestamp', sa.DateTime(), nullable=False),
    sa.Column('last_modification_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['by_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['rego_id'], ['registration.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_allocation',
    sa.Column('invoice_item_id', sa.Integer(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_item_id'], ['invoice_item.id'],onupdate='CASCADE', ondelete='CASCADE' ),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], onupdate='CASCADE', ondelete='CASCADE' ),
    sa.PrimaryKeyConstraint('invoice_item_id', 'payment_id')
    )
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment_allocation')
    op.drop_table('rego_note')
    op.drop_table('schedule')
    op.drop_table('payment_received')
    op.drop_table('registration_product_map')
    op.drop_table('voucher_product')
    op.drop_table('payment')
    op.drop_table('funding_review')
    op.drop_table('product_ceiling_map')
    op.drop_table('funding_attachment')
    op.drop_table('invoice_item')
    op.drop_table('attachment')
    op.drop_table('registration')
    op.drop_table('product_include')
    op.drop_table('volunteer')
    op.drop_table('event')
    op.drop_table('person_proposal_map')
    op.drop_table('review')
    op.drop_table('db_content')
    op.drop_table('product')
    op.drop_table('person_social_network_map')
    op.drop_table('voucher')
    op.drop_table('funding')
    op.drop_table('invoice')
    op.drop_table('special_registration')
    op.drop_table('proposal')
    op.drop_table('person_role_map')
    op.drop_table('time_slot')
    op.drop_table('role')
    op.drop_table('product_category')
    op.drop_table('social_network')
    op.drop_table('person')
    op.drop_table('event_type')
    op.drop_table('location')
    op.drop_table('ceiling')
    op.drop_table('proposal_status')
    op.drop_table('special_offer')
    op.drop_table('funding_status')
    op.drop_table('stream')
    op.drop_table('password_reset_confirmation')
    op.drop_table('funding_type')
    op.drop_table('db_content_type')
    op.drop_table('vote')
    op.drop_table('target_audience')
    op.drop_table('proposal_type')
    op.drop_table('accommodation_assistance_type')
    op.drop_table('travel_assistance_type')
    op.drop_table('url_hash')
    ### end Alembic commands ###
