from google.type import color_pb2 as _color_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Card(_message.Message):
    __slots__ = ("header", "sections", "section_divider_style", "card_actions", "name", "fixed_footer", "display_style", "peek_card_header")
    class DividerStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIVIDER_STYLE_UNSPECIFIED: _ClassVar[Card.DividerStyle]
        SOLID_DIVIDER: _ClassVar[Card.DividerStyle]
        NO_DIVIDER: _ClassVar[Card.DividerStyle]
    DIVIDER_STYLE_UNSPECIFIED: Card.DividerStyle
    SOLID_DIVIDER: Card.DividerStyle
    NO_DIVIDER: Card.DividerStyle
    class DisplayStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISPLAY_STYLE_UNSPECIFIED: _ClassVar[Card.DisplayStyle]
        PEEK: _ClassVar[Card.DisplayStyle]
        REPLACE: _ClassVar[Card.DisplayStyle]
    DISPLAY_STYLE_UNSPECIFIED: Card.DisplayStyle
    PEEK: Card.DisplayStyle
    REPLACE: Card.DisplayStyle
    class CardHeader(_message.Message):
        __slots__ = ("title", "subtitle", "image_type", "image_url", "image_alt_text")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        image_type: Widget.ImageType
        image_url: str
        image_alt_text: str
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., image_type: _Optional[_Union[Widget.ImageType, str]] = ..., image_url: _Optional[str] = ..., image_alt_text: _Optional[str] = ...) -> None: ...
    class Section(_message.Message):
        __slots__ = ("header", "widgets", "collapsible", "uncollapsible_widgets_count")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        COLLAPSIBLE_FIELD_NUMBER: _ClassVar[int]
        UNCOLLAPSIBLE_WIDGETS_COUNT_FIELD_NUMBER: _ClassVar[int]
        header: str
        widgets: _containers.RepeatedCompositeFieldContainer[Widget]
        collapsible: bool
        uncollapsible_widgets_count: int
        def __init__(self, header: _Optional[str] = ..., widgets: _Optional[_Iterable[_Union[Widget, _Mapping]]] = ..., collapsible: bool = ..., uncollapsible_widgets_count: _Optional[int] = ...) -> None: ...
    class CardAction(_message.Message):
        __slots__ = ("action_label", "on_click")
        ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
        ON_CLICK_FIELD_NUMBER: _ClassVar[int]
        action_label: str
        on_click: OnClick
        def __init__(self, action_label: _Optional[str] = ..., on_click: _Optional[_Union[OnClick, _Mapping]] = ...) -> None: ...
    class CardFixedFooter(_message.Message):
        __slots__ = ("primary_button", "secondary_button")
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        primary_button: Button
        secondary_button: Button
        def __init__(self, primary_button: _Optional[_Union[Button, _Mapping]] = ..., secondary_button: _Optional[_Union[Button, _Mapping]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    SECTION_DIVIDER_STYLE_FIELD_NUMBER: _ClassVar[int]
    CARD_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIXED_FOOTER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_STYLE_FIELD_NUMBER: _ClassVar[int]
    PEEK_CARD_HEADER_FIELD_NUMBER: _ClassVar[int]
    header: Card.CardHeader
    sections: _containers.RepeatedCompositeFieldContainer[Card.Section]
    section_divider_style: Card.DividerStyle
    card_actions: _containers.RepeatedCompositeFieldContainer[Card.CardAction]
    name: str
    fixed_footer: Card.CardFixedFooter
    display_style: Card.DisplayStyle
    peek_card_header: Card.CardHeader
    def __init__(self, header: _Optional[_Union[Card.CardHeader, _Mapping]] = ..., sections: _Optional[_Iterable[_Union[Card.Section, _Mapping]]] = ..., section_divider_style: _Optional[_Union[Card.DividerStyle, str]] = ..., card_actions: _Optional[_Iterable[_Union[Card.CardAction, _Mapping]]] = ..., name: _Optional[str] = ..., fixed_footer: _Optional[_Union[Card.CardFixedFooter, _Mapping]] = ..., display_style: _Optional[_Union[Card.DisplayStyle, str]] = ..., peek_card_header: _Optional[_Union[Card.CardHeader, _Mapping]] = ...) -> None: ...

class Widget(_message.Message):
    __slots__ = ("text_paragraph", "image", "decorated_text", "button_list", "text_input", "selection_input", "date_time_picker", "divider", "grid", "columns", "horizontal_alignment")
    class ImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQUARE: _ClassVar[Widget.ImageType]
        CIRCLE: _ClassVar[Widget.ImageType]
    SQUARE: Widget.ImageType
    CIRCLE: Widget.ImageType
    class HorizontalAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HORIZONTAL_ALIGNMENT_UNSPECIFIED: _ClassVar[Widget.HorizontalAlignment]
        START: _ClassVar[Widget.HorizontalAlignment]
        CENTER: _ClassVar[Widget.HorizontalAlignment]
        END: _ClassVar[Widget.HorizontalAlignment]
    HORIZONTAL_ALIGNMENT_UNSPECIFIED: Widget.HorizontalAlignment
    START: Widget.HorizontalAlignment
    CENTER: Widget.HorizontalAlignment
    END: Widget.HorizontalAlignment
    TEXT_PARAGRAPH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DECORATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    BUTTON_LIST_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    SELECTION_INPUT_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_PICKER_FIELD_NUMBER: _ClassVar[int]
    DIVIDER_FIELD_NUMBER: _ClassVar[int]
    GRID_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    text_paragraph: TextParagraph
    image: Image
    decorated_text: DecoratedText
    button_list: ButtonList
    text_input: TextInput
    selection_input: SelectionInput
    date_time_picker: DateTimePicker
    divider: Divider
    grid: Grid
    columns: Columns
    horizontal_alignment: Widget.HorizontalAlignment
    def __init__(self, text_paragraph: _Optional[_Union[TextParagraph, _Mapping]] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., decorated_text: _Optional[_Union[DecoratedText, _Mapping]] = ..., button_list: _Optional[_Union[ButtonList, _Mapping]] = ..., text_input: _Optional[_Union[TextInput, _Mapping]] = ..., selection_input: _Optional[_Union[SelectionInput, _Mapping]] = ..., date_time_picker: _Optional[_Union[DateTimePicker, _Mapping]] = ..., divider: _Optional[_Union[Divider, _Mapping]] = ..., grid: _Optional[_Union[Grid, _Mapping]] = ..., columns: _Optional[_Union[Columns, _Mapping]] = ..., horizontal_alignment: _Optional[_Union[Widget.HorizontalAlignment, str]] = ...) -> None: ...

class TextParagraph(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("image_url", "on_click", "alt_text")
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ON_CLICK_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    on_click: OnClick
    alt_text: str
    def __init__(self, image_url: _Optional[str] = ..., on_click: _Optional[_Union[OnClick, _Mapping]] = ..., alt_text: _Optional[str] = ...) -> None: ...

class Divider(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DecoratedText(_message.Message):
    __slots__ = ("icon", "start_icon", "top_label", "text", "wrap_text", "bottom_label", "on_click", "button", "switch_control", "end_icon")
    class SwitchControl(_message.Message):
        __slots__ = ("name", "value", "selected", "on_change_action", "control_type")
        class ControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SWITCH: _ClassVar[DecoratedText.SwitchControl.ControlType]
            CHECKBOX: _ClassVar[DecoratedText.SwitchControl.ControlType]
            CHECK_BOX: _ClassVar[DecoratedText.SwitchControl.ControlType]
        SWITCH: DecoratedText.SwitchControl.ControlType
        CHECKBOX: DecoratedText.SwitchControl.ControlType
        CHECK_BOX: DecoratedText.SwitchControl.ControlType
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        SELECTED_FIELD_NUMBER: _ClassVar[int]
        ON_CHANGE_ACTION_FIELD_NUMBER: _ClassVar[int]
        CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        selected: bool
        on_change_action: Action
        control_type: DecoratedText.SwitchControl.ControlType
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., selected: bool = ..., on_change_action: _Optional[_Union[Action, _Mapping]] = ..., control_type: _Optional[_Union[DecoratedText.SwitchControl.ControlType, str]] = ...) -> None: ...
    ICON_FIELD_NUMBER: _ClassVar[int]
    START_ICON_FIELD_NUMBER: _ClassVar[int]
    TOP_LABEL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    WRAP_TEXT_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_LABEL_FIELD_NUMBER: _ClassVar[int]
    ON_CLICK_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    SWITCH_CONTROL_FIELD_NUMBER: _ClassVar[int]
    END_ICON_FIELD_NUMBER: _ClassVar[int]
    icon: Icon
    start_icon: Icon
    top_label: str
    text: str
    wrap_text: bool
    bottom_label: str
    on_click: OnClick
    button: Button
    switch_control: DecoratedText.SwitchControl
    end_icon: Icon
    def __init__(self, icon: _Optional[_Union[Icon, _Mapping]] = ..., start_icon: _Optional[_Union[Icon, _Mapping]] = ..., top_label: _Optional[str] = ..., text: _Optional[str] = ..., wrap_text: bool = ..., bottom_label: _Optional[str] = ..., on_click: _Optional[_Union[OnClick, _Mapping]] = ..., button: _Optional[_Union[Button, _Mapping]] = ..., switch_control: _Optional[_Union[DecoratedText.SwitchControl, _Mapping]] = ..., end_icon: _Optional[_Union[Icon, _Mapping]] = ...) -> None: ...

class TextInput(_message.Message):
    __slots__ = ("name", "label", "hint_text", "value", "type", "on_change_action", "initial_suggestions", "auto_complete_action", "placeholder_text")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SINGLE_LINE: _ClassVar[TextInput.Type]
        MULTIPLE_LINE: _ClassVar[TextInput.Type]
    SINGLE_LINE: TextInput.Type
    MULTIPLE_LINE: TextInput.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    HINT_TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ON_CHANGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMPLETE_ACTION_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    label: str
    hint_text: str
    value: str
    type: TextInput.Type
    on_change_action: Action
    initial_suggestions: Suggestions
    auto_complete_action: Action
    placeholder_text: str
    def __init__(self, name: _Optional[str] = ..., label: _Optional[str] = ..., hint_text: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[_Union[TextInput.Type, str]] = ..., on_change_action: _Optional[_Union[Action, _Mapping]] = ..., initial_suggestions: _Optional[_Union[Suggestions, _Mapping]] = ..., auto_complete_action: _Optional[_Union[Action, _Mapping]] = ..., placeholder_text: _Optional[str] = ...) -> None: ...

class Suggestions(_message.Message):
    __slots__ = ("items",)
    class SuggestionItem(_message.Message):
        __slots__ = ("text",)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Suggestions.SuggestionItem]
    def __init__(self, items: _Optional[_Iterable[_Union[Suggestions.SuggestionItem, _Mapping]]] = ...) -> None: ...

class ButtonList(_message.Message):
    __slots__ = ("buttons",)
    BUTTONS_FIELD_NUMBER: _ClassVar[int]
    buttons: _containers.RepeatedCompositeFieldContainer[Button]
    def __init__(self, buttons: _Optional[_Iterable[_Union[Button, _Mapping]]] = ...) -> None: ...

class SelectionInput(_message.Message):
    __slots__ = ("name", "label", "type", "items", "on_change_action", "multi_select_max_selected_items", "multi_select_min_query_length", "external_data_source", "platform_data_source")
    class SelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHECK_BOX: _ClassVar[SelectionInput.SelectionType]
        RADIO_BUTTON: _ClassVar[SelectionInput.SelectionType]
        SWITCH: _ClassVar[SelectionInput.SelectionType]
        DROPDOWN: _ClassVar[SelectionInput.SelectionType]
        MULTI_SELECT: _ClassVar[SelectionInput.SelectionType]
    CHECK_BOX: SelectionInput.SelectionType
    RADIO_BUTTON: SelectionInput.SelectionType
    SWITCH: SelectionInput.SelectionType
    DROPDOWN: SelectionInput.SelectionType
    MULTI_SELECT: SelectionInput.SelectionType
    class SelectionItem(_message.Message):
        __slots__ = ("text", "value", "selected", "start_icon_uri", "bottom_text")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        SELECTED_FIELD_NUMBER: _ClassVar[int]
        START_ICON_URI_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        value: str
        selected: bool
        start_icon_uri: str
        bottom_text: str
        def __init__(self, text: _Optional[str] = ..., value: _Optional[str] = ..., selected: bool = ..., start_icon_uri: _Optional[str] = ..., bottom_text: _Optional[str] = ...) -> None: ...
    class PlatformDataSource(_message.Message):
        __slots__ = ("common_data_source",)
        class CommonDataSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[SelectionInput.PlatformDataSource.CommonDataSource]
            USER: _ClassVar[SelectionInput.PlatformDataSource.CommonDataSource]
        UNKNOWN: SelectionInput.PlatformDataSource.CommonDataSource
        USER: SelectionInput.PlatformDataSource.CommonDataSource
        COMMON_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
        common_data_source: SelectionInput.PlatformDataSource.CommonDataSource
        def __init__(self, common_data_source: _Optional[_Union[SelectionInput.PlatformDataSource.CommonDataSource, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ON_CHANGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    MULTI_SELECT_MAX_SELECTED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MULTI_SELECT_MIN_QUERY_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    label: str
    type: SelectionInput.SelectionType
    items: _containers.RepeatedCompositeFieldContainer[SelectionInput.SelectionItem]
    on_change_action: Action
    multi_select_max_selected_items: int
    multi_select_min_query_length: int
    external_data_source: Action
    platform_data_source: SelectionInput.PlatformDataSource
    def __init__(self, name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[_Union[SelectionInput.SelectionType, str]] = ..., items: _Optional[_Iterable[_Union[SelectionInput.SelectionItem, _Mapping]]] = ..., on_change_action: _Optional[_Union[Action, _Mapping]] = ..., multi_select_max_selected_items: _Optional[int] = ..., multi_select_min_query_length: _Optional[int] = ..., external_data_source: _Optional[_Union[Action, _Mapping]] = ..., platform_data_source: _Optional[_Union[SelectionInput.PlatformDataSource, _Mapping]] = ...) -> None: ...

class DateTimePicker(_message.Message):
    __slots__ = ("name", "label", "type", "value_ms_epoch", "timezone_offset_date", "on_change_action")
    class DateTimePickerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATE_AND_TIME: _ClassVar[DateTimePicker.DateTimePickerType]
        DATE_ONLY: _ClassVar[DateTimePicker.DateTimePickerType]
        TIME_ONLY: _ClassVar[DateTimePicker.DateTimePickerType]
    DATE_AND_TIME: DateTimePicker.DateTimePickerType
    DATE_ONLY: DateTimePicker.DateTimePickerType
    TIME_ONLY: DateTimePicker.DateTimePickerType
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MS_EPOCH_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_OFFSET_DATE_FIELD_NUMBER: _ClassVar[int]
    ON_CHANGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    label: str
    type: DateTimePicker.DateTimePickerType
    value_ms_epoch: int
    timezone_offset_date: int
    on_change_action: Action
    def __init__(self, name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[_Union[DateTimePicker.DateTimePickerType, str]] = ..., value_ms_epoch: _Optional[int] = ..., timezone_offset_date: _Optional[int] = ..., on_change_action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class Button(_message.Message):
    __slots__ = ("text", "icon", "color", "on_click", "disabled", "alt_text")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ON_CLICK_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    icon: Icon
    color: _color_pb2.Color
    on_click: OnClick
    disabled: bool
    alt_text: str
    def __init__(self, text: _Optional[str] = ..., icon: _Optional[_Union[Icon, _Mapping]] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., on_click: _Optional[_Union[OnClick, _Mapping]] = ..., disabled: bool = ..., alt_text: _Optional[str] = ...) -> None: ...

class Icon(_message.Message):
    __slots__ = ("known_icon", "icon_url", "material_icon", "alt_text", "image_type")
    KNOWN_ICON_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ICON_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    known_icon: str
    icon_url: str
    material_icon: MaterialIcon
    alt_text: str
    image_type: Widget.ImageType
    def __init__(self, known_icon: _Optional[str] = ..., icon_url: _Optional[str] = ..., material_icon: _Optional[_Union[MaterialIcon, _Mapping]] = ..., alt_text: _Optional[str] = ..., image_type: _Optional[_Union[Widget.ImageType, str]] = ...) -> None: ...

class MaterialIcon(_message.Message):
    __slots__ = ("name", "fill", "weight", "grade")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILL_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    name: str
    fill: bool
    weight: int
    grade: int
    def __init__(self, name: _Optional[str] = ..., fill: bool = ..., weight: _Optional[int] = ..., grade: _Optional[int] = ...) -> None: ...

class ImageCropStyle(_message.Message):
    __slots__ = ("type", "aspect_ratio")
    class ImageCropType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE_CROP_TYPE_UNSPECIFIED: _ClassVar[ImageCropStyle.ImageCropType]
        SQUARE: _ClassVar[ImageCropStyle.ImageCropType]
        CIRCLE: _ClassVar[ImageCropStyle.ImageCropType]
        RECTANGLE_CUSTOM: _ClassVar[ImageCropStyle.ImageCropType]
        RECTANGLE_4_3: _ClassVar[ImageCropStyle.ImageCropType]
    IMAGE_CROP_TYPE_UNSPECIFIED: ImageCropStyle.ImageCropType
    SQUARE: ImageCropStyle.ImageCropType
    CIRCLE: ImageCropStyle.ImageCropType
    RECTANGLE_CUSTOM: ImageCropStyle.ImageCropType
    RECTANGLE_4_3: ImageCropStyle.ImageCropType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
    type: ImageCropStyle.ImageCropType
    aspect_ratio: float
    def __init__(self, type: _Optional[_Union[ImageCropStyle.ImageCropType, str]] = ..., aspect_ratio: _Optional[float] = ...) -> None: ...

class BorderStyle(_message.Message):
    __slots__ = ("type", "stroke_color", "corner_radius")
    class BorderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BORDER_TYPE_UNSPECIFIED: _ClassVar[BorderStyle.BorderType]
        NO_BORDER: _ClassVar[BorderStyle.BorderType]
        STROKE: _ClassVar[BorderStyle.BorderType]
    BORDER_TYPE_UNSPECIFIED: BorderStyle.BorderType
    NO_BORDER: BorderStyle.BorderType
    STROKE: BorderStyle.BorderType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STROKE_COLOR_FIELD_NUMBER: _ClassVar[int]
    CORNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    type: BorderStyle.BorderType
    stroke_color: _color_pb2.Color
    corner_radius: int
    def __init__(self, type: _Optional[_Union[BorderStyle.BorderType, str]] = ..., stroke_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., corner_radius: _Optional[int] = ...) -> None: ...

class ImageComponent(_message.Message):
    __slots__ = ("image_uri", "alt_text", "crop_style", "border_style")
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    CROP_STYLE_FIELD_NUMBER: _ClassVar[int]
    BORDER_STYLE_FIELD_NUMBER: _ClassVar[int]
    image_uri: str
    alt_text: str
    crop_style: ImageCropStyle
    border_style: BorderStyle
    def __init__(self, image_uri: _Optional[str] = ..., alt_text: _Optional[str] = ..., crop_style: _Optional[_Union[ImageCropStyle, _Mapping]] = ..., border_style: _Optional[_Union[BorderStyle, _Mapping]] = ...) -> None: ...

class Grid(_message.Message):
    __slots__ = ("title", "items", "border_style", "column_count", "on_click")
    class GridItem(_message.Message):
        __slots__ = ("id", "image", "title", "subtitle", "layout")
        class GridItemLayout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GRID_ITEM_LAYOUT_UNSPECIFIED: _ClassVar[Grid.GridItem.GridItemLayout]
            TEXT_BELOW: _ClassVar[Grid.GridItem.GridItemLayout]
            TEXT_ABOVE: _ClassVar[Grid.GridItem.GridItemLayout]
        GRID_ITEM_LAYOUT_UNSPECIFIED: Grid.GridItem.GridItemLayout
        TEXT_BELOW: Grid.GridItem.GridItemLayout
        TEXT_ABOVE: Grid.GridItem.GridItemLayout
        ID_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_FIELD_NUMBER: _ClassVar[int]
        id: str
        image: ImageComponent
        title: str
        subtitle: str
        layout: Grid.GridItem.GridItemLayout
        def __init__(self, id: _Optional[str] = ..., image: _Optional[_Union[ImageComponent, _Mapping]] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., layout: _Optional[_Union[Grid.GridItem.GridItemLayout, str]] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BORDER_STYLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ON_CLICK_FIELD_NUMBER: _ClassVar[int]
    title: str
    items: _containers.RepeatedCompositeFieldContainer[Grid.GridItem]
    border_style: BorderStyle
    column_count: int
    on_click: OnClick
    def __init__(self, title: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Grid.GridItem, _Mapping]]] = ..., border_style: _Optional[_Union[BorderStyle, _Mapping]] = ..., column_count: _Optional[int] = ..., on_click: _Optional[_Union[OnClick, _Mapping]] = ...) -> None: ...

class Columns(_message.Message):
    __slots__ = ("column_items",)
    class Column(_message.Message):
        __slots__ = ("horizontal_size_style", "horizontal_alignment", "vertical_alignment", "widgets")
        class HorizontalSizeStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            HORIZONTAL_SIZE_STYLE_UNSPECIFIED: _ClassVar[Columns.Column.HorizontalSizeStyle]
            FILL_AVAILABLE_SPACE: _ClassVar[Columns.Column.HorizontalSizeStyle]
            FILL_MINIMUM_SPACE: _ClassVar[Columns.Column.HorizontalSizeStyle]
        HORIZONTAL_SIZE_STYLE_UNSPECIFIED: Columns.Column.HorizontalSizeStyle
        FILL_AVAILABLE_SPACE: Columns.Column.HorizontalSizeStyle
        FILL_MINIMUM_SPACE: Columns.Column.HorizontalSizeStyle
        class VerticalAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VERTICAL_ALIGNMENT_UNSPECIFIED: _ClassVar[Columns.Column.VerticalAlignment]
            CENTER: _ClassVar[Columns.Column.VerticalAlignment]
            TOP: _ClassVar[Columns.Column.VerticalAlignment]
            BOTTOM: _ClassVar[Columns.Column.VerticalAlignment]
        VERTICAL_ALIGNMENT_UNSPECIFIED: Columns.Column.VerticalAlignment
        CENTER: Columns.Column.VerticalAlignment
        TOP: Columns.Column.VerticalAlignment
        BOTTOM: Columns.Column.VerticalAlignment
        class Widgets(_message.Message):
            __slots__ = ("text_paragraph", "image", "decorated_text", "button_list", "text_input", "selection_input", "date_time_picker")
            TEXT_PARAGRAPH_FIELD_NUMBER: _ClassVar[int]
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            DECORATED_TEXT_FIELD_NUMBER: _ClassVar[int]
            BUTTON_LIST_FIELD_NUMBER: _ClassVar[int]
            TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
            SELECTION_INPUT_FIELD_NUMBER: _ClassVar[int]
            DATE_TIME_PICKER_FIELD_NUMBER: _ClassVar[int]
            text_paragraph: TextParagraph
            image: Image
            decorated_text: DecoratedText
            button_list: ButtonList
            text_input: TextInput
            selection_input: SelectionInput
            date_time_picker: DateTimePicker
            def __init__(self, text_paragraph: _Optional[_Union[TextParagraph, _Mapping]] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., decorated_text: _Optional[_Union[DecoratedText, _Mapping]] = ..., button_list: _Optional[_Union[ButtonList, _Mapping]] = ..., text_input: _Optional[_Union[TextInput, _Mapping]] = ..., selection_input: _Optional[_Union[SelectionInput, _Mapping]] = ..., date_time_picker: _Optional[_Union[DateTimePicker, _Mapping]] = ...) -> None: ...
        HORIZONTAL_SIZE_STYLE_FIELD_NUMBER: _ClassVar[int]
        HORIZONTAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        horizontal_size_style: Columns.Column.HorizontalSizeStyle
        horizontal_alignment: Widget.HorizontalAlignment
        vertical_alignment: Columns.Column.VerticalAlignment
        widgets: _containers.RepeatedCompositeFieldContainer[Columns.Column.Widgets]
        def __init__(self, horizontal_size_style: _Optional[_Union[Columns.Column.HorizontalSizeStyle, str]] = ..., horizontal_alignment: _Optional[_Union[Widget.HorizontalAlignment, str]] = ..., vertical_alignment: _Optional[_Union[Columns.Column.VerticalAlignment, str]] = ..., widgets: _Optional[_Iterable[_Union[Columns.Column.Widgets, _Mapping]]] = ...) -> None: ...
    COLUMN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    column_items: _containers.RepeatedCompositeFieldContainer[Columns.Column]
    def __init__(self, column_items: _Optional[_Iterable[_Union[Columns.Column, _Mapping]]] = ...) -> None: ...

class OnClick(_message.Message):
    __slots__ = ("action", "open_link", "open_dynamic_link_action", "card")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OPEN_LINK_FIELD_NUMBER: _ClassVar[int]
    OPEN_DYNAMIC_LINK_ACTION_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    action: Action
    open_link: OpenLink
    open_dynamic_link_action: Action
    card: Card
    def __init__(self, action: _Optional[_Union[Action, _Mapping]] = ..., open_link: _Optional[_Union[OpenLink, _Mapping]] = ..., open_dynamic_link_action: _Optional[_Union[Action, _Mapping]] = ..., card: _Optional[_Union[Card, _Mapping]] = ...) -> None: ...

class OpenLink(_message.Message):
    __slots__ = ("url", "open_as", "on_close")
    class OpenAs(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FULL_SIZE: _ClassVar[OpenLink.OpenAs]
        OVERLAY: _ClassVar[OpenLink.OpenAs]
    FULL_SIZE: OpenLink.OpenAs
    OVERLAY: OpenLink.OpenAs
    class OnClose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTHING: _ClassVar[OpenLink.OnClose]
        RELOAD: _ClassVar[OpenLink.OnClose]
    NOTHING: OpenLink.OnClose
    RELOAD: OpenLink.OnClose
    URL_FIELD_NUMBER: _ClassVar[int]
    OPEN_AS_FIELD_NUMBER: _ClassVar[int]
    ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
    url: str
    open_as: OpenLink.OpenAs
    on_close: OpenLink.OnClose
    def __init__(self, url: _Optional[str] = ..., open_as: _Optional[_Union[OpenLink.OpenAs, str]] = ..., on_close: _Optional[_Union[OpenLink.OnClose, str]] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("function", "parameters", "load_indicator", "persist_values", "interaction")
    class LoadIndicator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPINNER: _ClassVar[Action.LoadIndicator]
        NONE: _ClassVar[Action.LoadIndicator]
    SPINNER: Action.LoadIndicator
    NONE: Action.LoadIndicator
    class Interaction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERACTION_UNSPECIFIED: _ClassVar[Action.Interaction]
        OPEN_DIALOG: _ClassVar[Action.Interaction]
    INTERACTION_UNSPECIFIED: Action.Interaction
    OPEN_DIALOG: Action.Interaction
    class ActionParameter(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    LOAD_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    PERSIST_VALUES_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_FIELD_NUMBER: _ClassVar[int]
    function: str
    parameters: _containers.RepeatedCompositeFieldContainer[Action.ActionParameter]
    load_indicator: Action.LoadIndicator
    persist_values: bool
    interaction: Action.Interaction
    def __init__(self, function: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[Action.ActionParameter, _Mapping]]] = ..., load_indicator: _Optional[_Union[Action.LoadIndicator, str]] = ..., persist_values: bool = ..., interaction: _Optional[_Union[Action.Interaction, str]] = ...) -> None: ...
